import pytest
from utils.getyamldata import read_yaml
from config.path import Path
from utils.requests_util import Request
from utils.log import logger
import allure
from utils.getyamldata import write_yaml


class TestBanding:
    ice_banding =read_yaml(Path.test_pda_path, 'test_ice_banding')
    bwx_banding = read_yaml(Path.test_pda_path, 'test_bwx_banding')
    cold_banding = read_yaml(Path.test_pda_path, 'test_cold_banding')
    band_ice = read_yaml(Path.test_pda_path, 'band_ice')

    @allure.feature("获取空闲冰排")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("cold_banding", cold_banding)
    def test_cold_banding(self, get_free_cold, get_token, cold_banding, get_free_ice):
        url = cold_banding['url']
        data = [cold_banding['RFID']]
        title = cold_banding['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        for item in res['body']["obj"]:
            write_yaml(Path.test_pda_path, "band_ice", "data", {"iceRowInfoReqList": [item],"freezerInfoCode": get_free_ice['rfid'], "freezerInfoId":get_free_ice['id']})

        assert res['code'] == 200 and res['body']['msg'] == '成功'

    @allure.feature("获取空闲保温箱")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("bwx_banding", bwx_banding)
    def test_bwx_banding(self, get_free_bwx, get_token, bwx_banding):
        url = bwx_banding['url']
        data = [bwx_banding['RFID']]
        title = bwx_banding['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        assert res['code'] == 200 and res['body']['msg'] == '成功'

    @allure.feature("获取空闲冷柜")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("ice_banding", ice_banding)
    def test_ice_banding(self,get_free_ice, get_token, ice_banding):
        url = ice_banding['url']
        data = [ice_banding['RFID']]
        title = ice_banding['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        assert res['code'] == 200 and res['body']['msg'] == '成功'


    @allure.feature("绑定冷柜")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("band_ice", band_ice)
    def test_band_ice(self, get_token, band_ice):
        url = band_ice['url']
        data = band_ice['data']
        title = band_ice['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        assert res['code'] == 200 and res['body']['msg'] == '成功'








