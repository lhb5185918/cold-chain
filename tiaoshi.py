import json

import pytest
import requests
from utils.getyamldata import read_yaml, write_yaml
from config.path import Path
import random
import json

#
# url = read_yaml(Path.config_file_path, 'token', 'token_url')
# headers = {"Content-Type": read_yaml(Path.config_file_path, 'token', "Content-Type")}
# data = read_yaml(Path.config_file_path, 'token', 'data')
# res = requests.post(url=url, headers=headers, json=data).json()
# print(url)
# print(headers)
# print(res['obj']['token'])


url = "http://bswms-uat-01.baheal.com:7777/bp/pda/equipmentQuery/getIceRowInfoList"
data = ["296281449"]
headers = {"Content-type": "application/json",
           "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJsaGIiLCJjcmVhdGVkIjoxNzE3NzMwMzIzNjk0LCJjb21wYW55TmFtZSI6IumdkuWym-eZvua0i-WMu-iNr-iCoeS7veaciemZkOWFrOWPuCIsImNvbXBhbnlTaG9ydE5hbWUiOiLpnZLlspvnmb7mtIvljLvoja_ogqHku73mnInpmZDlhazlj7giLCJ1c2VySWQiOjE3MDk1OTkwNzA4Njc5NjgsInN1cHBlciI6dHJ1ZSwid2FyZWhvdXNlTmFtZSI6IumdkuWym-S7kyIsImNsaWVudF9pZCI6IlJGSURfUERBIiwid2FyZWhvdXNlQ29kZSI6IlFEQyIsInVzZXJfbm8iOiJsaGIiLCJjdXJyZW50X3VzZXJfbmFtZSI6Iuadjum4v-WuviIsInVzZXJMYW5ndWFnZSI6InpoLUNOIiwiYXVkIjpbInpocWMiXSwiY29tcGFueUlkIjo4MTc5MjY5Mzg0NjQ3NjgsImxvZ2luVGltZSI6MTcxNzczMDMyMzU5NywibW9kaWZ5VGltZSI6MTcxMzc3NjI2OTAwMCwid2FyZWhvdXNlSWQiOiI4MTc5Mjk5NDAzNDEyNDgiLCJzY29wZSI6WyJhbGwiXSwiY29tcGFueV9jb2RlIjoiUURCWVlZR0YiLCJleHAiOjE3MTc3NjYzMjMsInBsYXRGb3JtIjoiYXBwIiwianRpIjoiN2Q2YTY5YzQtM2U3OC00NmZiLTlhNmUtNTllYjIzYTRlMzQzIiwiZGF0YVBlcm1pc3Npb24iOiJ7fSJ9.cwdBtj6qAVFBFbpNS5AV-88oj5vs3hXkYt5PIleznTMt_Y2OOHDdpzFpmYkBpbq91V0vG2ri9_XDxiF_y-CNq926rhO9PzpJQN6ngcZBa5nSnPYqqAaSAkDvGavKHpQBMGsyCa0MISHCx0Zi3-uPeh7I4jLrX3txZ4L7WBvtGq3qQlv-d4X03v-XFl7LJUat1l2uGcWHnl2wzgzOg55HNSzNJE558bUkaGS-IyPr_9flU8ffwFofLIOY0Kh866oveLcbE21l6raqDFB4tjxLNdj-bCGAcTMex-zeXhDWet9R4WByYFmO8jELzvd_46vPoERFiCnEtE45cTtRIbBFYg"}
res = requests.post(url=url, data=json.dumps(data), headers=headers).json()
for i in res['obj']:
    print(i['imageList'])

