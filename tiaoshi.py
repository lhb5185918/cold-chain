import pytest
import requests
from utils.getyamldata import read_yaml
from config.path import Path
#
# url = read_yaml(Path.config_file_path, 'token', 'token_url')
# headers = {"Content-Type": read_yaml(Path.config_file_path, 'token', "Content-Type")}
# data = read_yaml(Path.config_file_path, 'token', 'data')
# res = requests.post(url=url, headers=headers, json=data).json()
# print(url)
# print(headers)
# print(res['obj']['token'])

res = read_yaml(Path.test_pda_path,"band_ice")
for i in res:
    print(i)