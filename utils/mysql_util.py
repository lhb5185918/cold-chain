import pymysql
from config.path import Path
from utils.getyamldata import *


class CommonDatabase():
    # ... existing code ...

    def config(self, key=None, value=None, update=None):
        self.database_config = {
            'host': read_yaml(Path.config_file_path, 'databaseconfig', 'host'),
            'user': read_yaml(Path.config_file_path, 'databaseconfig', 'user'),
            'password': read_yaml(Path.config_file_path, 'databaseconfig', 'password'),
            'db': read_yaml(Path.config_file_path, 'databaseconfig', 'db'),
            'charset': read_yaml(Path.config_file_path, 'databaseconfig', 'charset'),
            'port': read_yaml(Path.config_file_path, 'databaseconfig', 'port'),
        }
        if update is None:
            return self.database_config
        else:
            self.database_config.update({key: value})
            return self.database_config
        # ... existing code ...

    def select_data(self, value, table_name, condition=None):
        self.conn = pymysql.connect(
            host=self.config()['host'],
            user=self.config()['user'],
            password=self.config()['password'],
            db=self.config()['db'],
            charset=self.config()['charset'],
            port=self.config()['port'],
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        try:
            if condition is not None:
                sql = f"select {value} from {table_name} where {condition}"
            else:
                sql = f"select {value} from {table_name}"
            self.cursor.execute(sql)
            self.conn.close()
            return self.cursor.fetchone()
        except Exception as e:
            return e

    def delete_data(self, table_name, condition=None):
        self.conn = pymysql.connect(
            host=self.config()['host'],
            user=self.config()['user'],
            password=self.config()['password'],
            db=self.config()['db'],
            charset=self.config()['charset'],
            port=self.config()['port'],
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        try:
            if condition is not None:
                sql = f"DELETE FROM {table_name} where {condition}"
            else:
                sql = f"DELETE FROM {table_name}"
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            return e
        finally:
            self.conn.close()

