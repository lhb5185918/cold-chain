import pytest
import requests
from utils.getyamldata import read_yaml, write_yaml
from config.path import Path


@pytest.fixture(scope="class")
# 获取token
def get_token():
    url = read_yaml(Path.config_file_path, 'token', 'token_url')
    headers = {"Content-Type": read_yaml(Path.config_file_path, 'token', "Content-Type")}
    data = read_yaml(Path.config_file_path, 'token', 'data')
    res = requests.post(url=url, headers=headers, json=data).json()
    token = {"Authorization": res['obj']['token']}
    return token


@pytest.fixture(scope="class")
# 获取空闲冰排数据
def get_free_cold(get_token):
    url = "http://bswms-uat-01.baheal.com:7777/bp/base/iceRowInfo/pageInfo"
    data = {"orderByColumnList": None, "equipmentCode": "testcold1", "iceRowCategoryId": None, "workStatus": None, "isEnable": None,"rfid": None, "page": 1, "limit": 50}
    if data['workStatus'] is not None :
        ValueError("冰排状态非空闲")
    res = requests.post(url=url, json=data, headers=get_token).json()
    for item in res['obj']:
        if item['workStatus'] != '空闲':
            ValueError("冰排状态非空闲")
            write_yaml(Path.test_pda_path,"test_cold_banding","RFID",item['rfid'])
        return item


@pytest.fixture(scope="class")
# 获取空闲保温箱数据
def get_free_bwx(get_token):
    url = "http://bswms-uat-01.baheal.com:7777/bp/base/incubatorInfo/pageInfo"
    data = {"orderByColumnList": None, "equipmentCode": "bwx1", "incubatorCategoryId": None, "workStatus": None, "isEnable": None, "rfid": None, "page": 1, "limit": 50}
    if data['workStatus'] is not None:
        ValueError("保温箱状态非空闲")
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
    data = {"orderByColumnList": None, "equipmentCode": "T0", "freezerCategoryId": None,"workStatus": None, "isEnable": None,"rfid": None, "page": 1, "limit": 50}
    if data['workStatus'] is not None:
        ValueError("冰排状态非空闲")
    res = requests.post(url=url, json=data, headers=get_token).json()
    for item in res['obj']:
        if item['workStatus'] != '空闲':
            ValueError("冰排状态非空闲")
            write_yaml(Path.test_pda_path, "test_ice_banding", "RFID",item['rfid'])
        return item


