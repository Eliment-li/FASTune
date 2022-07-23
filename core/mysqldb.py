import os
import pdb
import time
import threading
import subprocess
# import paramiko
import logging
import numpy as np
import multiprocessing as mp
from getpass import getpass
# from autotune.dbconnector import MysqlConnector
# from autotune.knobs import logger
# from autotune.utils.parser import ConfigParser
# from autotune.knobs import initialize_knobs, get_default_knobs
from loguru import logger

dst_data_path = os.environ.get("DATADST")
src_data_path = os.environ.get("DATASRC")
log_num_default = 2
log_size_default = 50331648

RESTART_WAIT_TIME = 5
TIMEOUT_CLOSE = 60


class MysqlDB:
    def __init__(self, args):
        self.args = args

        # MySQL configuration
        self.host = args['host']
        self.port = args['port']
        self.user = args['user']
        self.passwd = args['passwd']
        self.dbname = args['dbname']
        self.sock = args['sock']
        self.pid = int(args['pid'])
        self.mycnf = args['cnf']
        self.mysqld = args['mysqld']

