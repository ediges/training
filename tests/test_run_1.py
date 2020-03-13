import logging

logger = logging.getLogger()


# @pytest.mark.skip
# def test_credentials(user_credentials):
#     # print('Test name: ' + inspect.currentframe().f_code.co_name)
#     print('\neco_admin_access_token inside test: ' + conftest.eco_admin_access_token)
#     print('eco_admin_refresh_token inside test: ' + conftest.eco_admin_refresh_token)
#     # assert user_credentials.get('username') == 'autoadmin'
#     pass
#
#
# # @pytestrail.case('C12666499')
# def test_credentials_2_1(user_credentials):
#     assert 1 == 2
#
#

# # @pytestrail.case('C12666205')
# @is_active(token='eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhdXRvYWRtaW4iLCJBdXRob3JpdGllcyI6WyJST0xFX0FETUlOIl0sImV4cCI6MTU3MjM2MzI4MywiaWF0IjoxNTcyMzYyNjgzfQ.ymkT6BgI_yjqvx2bo24etd19t1AvhmrXgHWbCJvtu3aBrjNco1k4ut_74RNiuUCmXw7IPZ7ez-WsGjOK4qZ-1Q')
# @is_active(token=t)
def test_token_3(get_eco_admin_access_token):
    print('stash1')
    logger.info('Running test... with token: ' + get_eco_admin_access_token)
    assert 0

# @log
# def my_calculations(a, b):
#     print("\na = " + str(a))
#     print("\nb = " + str(b))
#     return a+b


# @log
# def print_message(message):
#     print("\n" + message)
#     return message + ' was returned'


# and here is how we decorate it
# @pytest.mark.parametrize("message", ['m1', 'm2'])
# def test_func(message):
#     print(print_message(message))


# @log
# def test_func_2():
#     print('--> Result: {}'.format(str(my_calculations(1, 2))))
