import pytest
import requests
from utils.getyamldata import read_yaml, write_yaml
from config.path import Path
import random
import json


@pytest.fixture(scope="class")
# 获取token
def get_token():
    url = read_yaml(Path.config_file_path, 'token', 'token_url')
    headers = {"Content-Type": read_yaml(Path.config_file_path, 'token', "Content-Type")}
    data = read_yaml(Path.config_file_path, 'token', 'data')
    res = requests.post(url=url, headers=headers, json=data).json()
    token = {"Authorization": res['obj']['token'], "Content-Type": "application/json"}
    return token


@pytest.fixture(scope="class")
def data_test(get_token):
    # 创建新冰排所需RFID数据
    test_rfid = random.randint(100000000, 300000000)
    if read_yaml(Path.test_file_path, "test_cold_add", "title") == "冰排资料新增":
        write_yaml(Path.test_file_path, "test_cold_add", "data",
                   {"isEnable": 1, "workStatus": 10, "equipmentCode": f"{test_rfid}",
                    "equipmentName": "testddata",
                    "iceRowCategoryId": "1764825015063040", "coldStorageDuration": 0.1, "releaseColdDuration": 0.1,
                    "releaseColdDurationMax": None, "weight": None, "innerLength": None, "innerWidth": None,
                    "innerHeight": None, "innerVolume": None, "externalLength": None, "externalWidth": None,
                    "externalHeight": None, "externalVolume": None, "factoryModel": None,
                    "phaseTransitionTemperature": None, "rfid": f"{test_rfid}", "imageList": []})
    return test_rfid


@pytest.fixture(scope="class")
# 获取空闲冰排数据
def test_rfid(get_token):
    test_rfid = read_yaml(Path.test_file_path, "test_cold_add", "data")['equipmentCode']
    data = {"orderByColumnList": None, "equipmentCode": f"{test_rfid}", "page": 1, "limit": 50}
    res = requests.post(url="http://bswms-uat-01.baheal.com:7777/bp/base/iceRowInfo/pageInfo", json=data,
                        headers=get_token).json()
    for item in res['obj']:
        return item


@pytest.fixture(scope="class")
# 获取空闲保温箱数据
def get_free_bwx(get_token):
    url = "http://bswms-uat-01.baheal.com:7777/bp/base/incubatorInfo/pageInfo"
    data = {"orderByColumnList": None, "equipmentCode": "bwx1", "incubatorCategoryId": None, "workStatus": None,
            "isEnable": None, "rfid": None, "page": 1, "limit": 50}
    if data['workStatus'] is not None:
        raise ValueError("保温箱状态非空闲")
    res = requests.post(url=url, json=data, headers=get_token).json()
    for item in res['obj']:
        if item['workStatus'] != '空闲':
            ValueError("保温箱状态非空闲")
            write_yaml(Path.test_pda_path, "test_bwx_banding", "RFID", item['rfid'])
        return item


@pytest.fixture(scope="class")
# 获取空闲冷柜数据
def get_free_ice(get_token):
    url = "http://bswms-uat-01.baheal.com:7777/bp/base/freezerInfo/pageInfo"
    data = {"orderByColumnList": None, "equipmentCode": "T0", "freezerCategoryId": None, "workStatus": None,
            "isEnable": None, "rfid": None, "page": 1, "limit": 50}
    if data['workStatus'] is not None:
        raise ValueError("冰排状态非空闲")
    res = requests.post(url=url, json=data, headers=get_token).json()
    for item in res['obj']:
        if item['workStatus'] != '空闲':
            write_yaml(Path.test_pda_path, "test_ice_banding", "RFID", item['rfid'])
            return item


@pytest.fixture(scope="class")
# pda查询冰排接口--冰排蓄冷时长、释冷时长取值
def pda_cold_select(get_token, test_rfid):
    url = "http://bswms-uat-01.baheal.com:7777/bp/pda/equipmentQuery/getIceRowInfoList"
    data = json.dumps([test_rfid['rfid']])
    res = requests.post(url=url, data=data, headers=get_token).json()
    for item in res['obj']:
        return item
