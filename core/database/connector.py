import mysql.connector
from abc import ABC, abstractmethod


class DBConnector(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def connect_db(self):
        pass

    @abstractmethod
    def close_db(self):
        pass

    @abstractmethod
    def fetch_results(self, sql, json=True):
        pass

    @abstractmethod
    def execute(self, sql):
        pass



class MysqlConnector(DBConnector):
    def __init__(self, host='192.168.3.128', port=3306, user='root', passwd='', name='sysbench', socket=''):
        super().__init__()
        self.db_host = host
        self.db_port = port
        self.db_user = user
        self.db_passwd = passwd
        self.db_name = name
        self.sock = socket
        self.conn = self.connect_db()
        if self.conn:
            self.cursor = self.conn.cursor()

    def connect_db(self):
        conn = False
        if self.sock:
            conn = mysql.connector.connect(host=self.db_host,
                                           user=self.db_user,
                                           passwd=self.db_passwd,
                                           db=self.db_name,
                                           port=self.db_port,
                                           unix_socket=self.sock)
        else:
            conn = mysql.connector.connect(host=self.db_host,
                                           user=self.db_user,
                                           passwd=self.db_passwd,
                                           db=self.db_name,
                                           port=self.db_port)
        return conn

    def close_db(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def fetch_results(self, sql, json=True):
        results = False
        if self.conn:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            if json:
                columns = [col[0] for col in self.cursor.description]
                return [dict(zip(columns, row)) for row in results]
        return results

    def execute(self, sql):
        results = False
        if self.conn:
            self.cursor.execute(sql)

if __name__ == '__main__':
    mysql=MysqlConnector(passwd='')
    print(mysql.conn.is_connected())
    sql = ' select count(id) as cnt from sbtest1'
    res = mysql.fetch_results(sql, json=True)
    print(res)
