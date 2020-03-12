from builtins import print
from classes.ApiRun import *
from config.EndPoints import *

import pytest
import logging

logging.basicConfig(filemode='w', filename='logging.log', level=logging.DEBUG, format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger()


# Global variables
eco_admin_access_token = None
eco_admin_refresh_token = None
BASE_PATH = None


def pytest_runtest_setup(item):
    logger.info(f"--> Test {item.nodeid} - Set up...")


def pytest_runtest_teardown(item):
    logger.info(f"--> Test {item.nodeid} - Tear down...")


def pytest_runtest_logreport(report):
    if report.when == 'call':
        if report.passed:
            # print("\ncase_id: " + case_id)
            print('\n-->Test "{}" PASSED'.format(report.nodeid))
        elif report.failed:
            # print("\ncase_id: " + case_id)
            print('\n-->Test "{}" FAILED'.format(report.nodeid))
        else:
            # print("\ncase_id: " + case_id)
            print('\n-->Test "{}" SKIPPED'.format(report.nodeid))


# @pytest.fixture(scope='session', autouse=True)
# @pytest.fixture(scope='session')
def session_start_up(user_credentials):
    logger.info('----------- Session start up -----------')

    global BASE_PATH
    BASE_PATH = 'https://demo.iot.sectigo.com/'

    tokens = get_tokens(BASE_PATH + AUTH_API, user_credentials)
    # tokens = get_tokens(AUTH_API_2, user_credentials)

    global eco_admin_access_token
    global eco_admin_refresh_token
    eco_admin_access_token = tokens.json().get('accessToken')
    eco_admin_refresh_token = tokens.json().get('refreshToken')

    yield

    # print('\nTest status is: ' + str(test_status))
    logger.info('----------- Session tear down -----------')


@pytest.fixture(scope="session")
def get_eco_admin_access_token(user_credentials):
    logger.debug("===+++===>   get_eco_admin_access_token startup...")

    global BASE_PATH
    BASE_PATH = 'https://demo.iot.sectigo.com/'
    tokens = get_tokens(BASE_PATH + AUTH_API, user_credentials)

    yield tokens.json().get('accessToken')

    logger.debug("===+++===> get_eco_admin_access_token teardown...")


@pytest.fixture(autouse=True)
def test_status(request):
    """Prints running test name - FOR FURTHER USE"""
    print('Test name: ' + str(request.function.__name__))


@pytest.fixture(scope='session')
def user_credentials():
    logger.debug("------->   Getting User Credentials...")
    credentials = {'username': 'autoadmin', 'password': '123456'}
    return credentials


# def get_eco_admin_access_token():
#     return eco_admin_access_token
#
#
# def get_eco_admin_refresh_token():
#     return eco_admin_refresh_token
#
#
# def get_base_path():
#     return BASE_PATH



