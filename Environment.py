import os
import socket
import logging
from configparser import ConfigParser
from datetime import date

#######################################################################################
# Config                                                             #
#######################################################################################

config = ConfigParser(allow_no_value=True)
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CRED_PATH = ROOT_PATH+'/cred'
img_upload_cred_path = f'{CRED_PATH}/google_storage_cert.json'
img_folder = ROOT_PATH+'/imgs/'
config.read(ROOT_PATH + '/config.ini')
# LOG_DIR = ROOT_PATH + '/log/'
# if not os.path.exists(LOG_DIR):
#     os.mkdir(LOG_DIR)

result_csv = f'{ROOT_PATH}/result.csv'


TIME_SLEEP = 10
SELENIUM_TIME_OUT = 300

#################################
# ENVIRONMENT VARIABLES
#################################
ConfigSectionPrefix = 'PROD_'
CHROME_DRIVER = config.get(ConfigSectionPrefix + 'CHROME_PATH', 'chrome_driver')
