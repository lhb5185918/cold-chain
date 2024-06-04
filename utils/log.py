import logging
import os
from config.path import Path
import time
class Log_util:
    def __init__(self):
        self.logger = logging.getLogger("logger")#创建logger对象
        self.logger.setLevel(logging.INFO)#设置日志输出等级
        self.log_name ='{}.log'.format(time.strftime("%Y_%m_%d"))#设置日志名称，设置日志格式
        self.log_path_file = os.path.join(Path.log_path, self.log_name)#创建日志文件
        fh = logging.FileHandler(self.log_path_file,encoding='utf-8',mode='w')#创建文件输入实例
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        fh.close()
        '''fh_stream = logging.StreamHandler()
        fh_stream.setLevel(logging.DEBUG)
        fh_stream.setFormatter(formatter)
        self.logger.addHandler(fh_stream)'''
    def log(self):
        return self.logger


logger = Log_util().log()