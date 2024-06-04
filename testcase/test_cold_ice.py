import pytest
from utils.getyamldata import read_yaml
from config.path import Path
from utils.requests_util import Request
from utils.log import logger
import allure
import time


class TestColdIce:
    cold_data = read_yaml(Path.test_file_path, 'cold_ice')
    bwx_data = read_yaml(Path.test_file_path, 'bwx_test')
    ice_data = read_yaml(Path.test_file_path, 'cold_test')
    ice_add = read_yaml(Path.test_file_path, 'test_ice_add')
    bwx_add = read_yaml(Path.test_file_path, 'test_bwx_add')
    cold_add = read_yaml(Path.test_file_path, 'test_cold_add')

    @allure.feature("冰排新增")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("cold_data", cold_data)
    # 冰排设备型号用例
    def test_cold(self, cold_data, get_token):
        url = cold_data['url']
        data = cold_data['data']
        title = cold_data['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        if title == '冰排设备型号重复新增':
            assert res['code'] == 200 and res['body']['msg'] == '设备型号已存在'
        elif title == '冰排设备型号正常新增':
            assert res['code'] == 200 and res['body']['msg'] == '成功'
        elif title == '冰排缺失必填项新增':
            assert res['code'] == 200 and res['body']['msg'] == '参数错误[设备型号不能为空]'
        elif title == '冰排设备型号过长新增':
            assert res['code'] == 200 and res['body']['msg'] == '参数错误[设备型号长度不能超过60]'
    time.sleep(1)

    @allure.feature("保温箱新增")
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("bwx_data", bwx_data)
    # 保温箱设备型号用例
    def test_bwx(self, bwx_data, get_token):
        url = bwx_data['url']
        data = bwx_data['data']
        title = bwx_data['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        if title == '保温箱重复新增':
            assert res['code'] == 200 and res['body']['msg'] == '设备型号已存在'
        elif title == '保温箱正常新增':
            assert res['code'] == 200 and res['body']['msg'] == '成功'
        elif title == '保温箱缺失必填项新增':
            assert res['code'] == 200 and res['body']['msg'] == '参数错误[设备型号不能为空]'
        elif title == '保温箱过长新增':
            assert res['code'] == 200 and res['body']['msg'] == '参数错误[设备型号长度不能超过60]'
    time.sleep(1)

    @allure.feature("冷柜新增")
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize("ice_data", ice_data)
    # 冷柜设备型号用例
    def test_ice(self, ice_data, get_token):
        url = ice_data['url']
        data = ice_data['data']
        title = ice_data['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        if title == '冷柜重复新增':
            assert res['code'] == 200 and res['body']['msg'] == '设备型号已存在'
        elif title == '冷柜正常新增':
            assert res['code'] == 200 and res['body']['msg'] == '成功'
        elif title == '冷柜缺失必填项新增':
            assert res['code'] == 200 and res['body']['msg'] == '参数错误[设备不能为空]'
        elif title == '冷柜过长新增':
            assert res['code'] == 200 and res['body']['msg'] == '参数错误[设备型号长度不能超过60]'
    time.sleep(1)

    @allure.feature("冰排资料新增")
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize("cold_add", cold_add)
    # 冰排资料新增用例
    def test_cold_add(self, cold_add, get_token):
        url = cold_add['url']
        data = cold_add['data']
        title = cold_add['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        if title == '冰排资料重复新增':
            assert res['code'] == 200 and res['body']['msg'] == '设备型号已存在'
        elif title == '冰排资料新增':
            assert res['code'] == 200 and res['body']['msg'] == '成功'
        elif title == '冰排资料缺失必填项新增':
            assert res['code'] == 200 and res['body']['msg'] == '参数错误[设备编码不能为空]'
    time.sleep(1)

    @allure.feature("保温箱资料新增")
    @pytest.mark.run(order=8)
    @pytest.mark.parametrize("bwx_add", bwx_add)
    # 保温箱资料新增用例
    def test_bwx_add(self, bwx_add, get_token):
        url = bwx_add['url']
        data = bwx_add['data']
        title = bwx_add['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        if title == '保温箱资料重复新增':
            assert res['code'] == 200 and res['body']['msg'] == '设备型号已存在'
        elif title == '保温箱资料新增':
            assert res['code'] == 200 and res['body']['msg'] == '成功'
        elif title == '保温箱资料缺失必填项新增':
            assert res['code'] == 200 and res['body']['msg'] == '参数错误[设备编码不能为空]'
    time.sleep(1)

    @allure.feature("冷柜资料新增")
    @pytest.mark.run(order=9)
    @pytest.mark.parametrize("ice_add", ice_add)
    # 冷柜资料新增用例
    def test_ice_add(self, ice_add, get_token):
        url = ice_add['url']
        data = ice_add['data']
        title = ice_add['title']
        res = Request().send(url=url, method='post', data=data, header=get_token)
        logger.info("{} {} {} ".format(title, res['body'], res['code']))
        if title == '冷柜资料重复新增':
            assert res['code'] == 200 and res['body']['msg'] == '设备型号已存在'
        elif title == '冷柜资料新增':
            assert res['code'] == 200 and res['body']['msg'] == '成功'
        elif title == '冷柜资料缺失必填项新增':
            assert res['code'] == 200 and res['body']['msg'] == '参数错误[设备编码不能为空]'
    time.sleep(1)



