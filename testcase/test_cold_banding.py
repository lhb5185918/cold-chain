import time
import pytest
from utils.getyamldata import read_yaml
from config.path import Path
from utils.requests_util import Request
from utils.log import logger
import allure
from utils.getyamldata import write_yaml
import asyncio


class TestBanding:
    ice_banding = read_yaml(Path.test_pda_path, 'test_ice_banding')
    bwx_banding = read_yaml(Path.test_pda_path, 'test_bwx_banding')
    cold_banding = read_yaml(Path.test_pda_path, 'test_cold_banding')
    band_ice = read_yaml(Path.test_pda_path, 'band_ice')
    un_band_ice = read_yaml(Path.test_pda_path, 'un_band_ice')

    @allure.feature("获取空闲冰排")
    @pytest.mark.run(order=9)
    @pytest.mark.parametrize("cold_banding", cold_banding)
    def test_cold_banding(self, get_token, cold_banding, get_free_ice, test_rfid):
        url = cold_banding['url']
        data = [test_rfid['rfid']]
        title = cold_banding['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        for item in res['body']["obj"]:
            write_yaml(Path.test_pda_path, "band_ice", "data",
                       {"iceRowInfoReqList": [item], "freezerInfoCode": get_free_ice['rfid'],
                        "freezerInfoId": int(get_free_ice['id'])})

        assert res['code'] == 200 and res['body']['msg'] == '成功'

    @allure.feature("获取空闲保温箱")
    @pytest.mark.run(order=10)
    @pytest.mark.parametrize("bwx_banding", bwx_banding)
    def test_bwx_banding(self, get_free_bwx, get_token, bwx_banding):
        url = bwx_banding['url']
        data = [bwx_banding['RFID']]
        title = bwx_banding['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        assert res['code'] == 200 and res['body']['msg'] == '成功'

    @allure.feature("获取空闲冷柜")
    @pytest.mark.run(order=11)
    @pytest.mark.parametrize("ice_banding", ice_banding)
    def test_ice_banding(self, get_free_ice, get_token, ice_banding):
        url = ice_banding['url']
        data = [ice_banding['RFID']]
        title = ice_banding['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        assert res['code'] == 200 and res['body']['msg'] == '成功'

    @allure.feature("绑定冷柜")
    @pytest.mark.run(order=12)
    @pytest.mark.parametrize("band_ice", band_ice)
    def test_band_ice(self, get_token, band_ice):
        url = band_ice['url']
        data = band_ice['data']
        title = band_ice['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        assert res['code'] == 200 and res['body']['msg'] == '成功'

    @allure.feature("解绑冷柜")
    @pytest.mark.run(order=13)
    @pytest.mark.asyncio
    @pytest.mark.parametrize("un_band_ice", un_band_ice)
    async def test_un_band_ice(self, get_token, un_band_ice, test_rfid, pda_cold_select):
        if pda_cold_select['coldStorageDurationMin'] is None:
            pda_cold_select['coldStorageDurationMin'] = 0.0
        if pda_cold_select['coldStorageDuration'] <= pda_cold_select['coldStorageDurationMin']:
            await asyncio.sleep(100)
            url = un_band_ice['url']
            data = [test_rfid['id']]
            title = un_band_ice['title']
            res = Request().send(url=url, method='post', data=data, header=get_token)
            logger.info("{} {} {} ".format(title, res['body'], res['code']))
            assert res['code'] == 200 and res['body']['msg'] == '成功'
