import yaml
from config.path import Path
import json


def read_yaml(file_path, key=None, value=None):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        if key is None:
            return data
        else:
            if value is None:
                return data[key]
            else:
                for item in data[key]:
                    if value is None:
                        return item
                    else:
                        return item[value]


def write_yaml(file_path, moudle_name, key, value):
    # 读取YAML文件
    with open(file_path, 'r', encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # 遍历数据并修改指定的字段
    for item in data[moudle_name]:
        if key in item:
            item[key] = value

    # 将修改后的内容写回到YAML文件中
    with open(file_path, 'w', encoding="utf-8") as file:
        yaml.safe_dump(data, file, default_flow_style=False, allow_unicode=True)
    return data

print(read_yaml(Path.test_file_path, 'test_cold_add',"data")['equipmentCode'])