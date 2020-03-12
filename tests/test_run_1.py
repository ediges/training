import pytest
import logging

from pytest_testrail.plugin import pytestrail

logger = logging.getLogger()

data = {
    'loginName': 'loginName',
    'loginPassword': 'loginPassword',
    'product': '279',
    'days': 365,
    'csr': '',
    'serverSoftware': -1,
    'emailAddress': 'admin@email.com',
    'validationEmailAddress': 'admin@email.com',
    'contactEmailAddress': 'admin@yahoo.com',
    'isCustomerValidated': 'N',
    'primaryDomainName': 'google',
    'responseFormat': 1,
}


def update_data(data_dict, **kwargs):
    for k, v in kwargs.items():
        if v is None:
            del data_dict[k]
        else:
            data_dict[k] = v
    return data_dict


update_args_input = [
    {'loginName': 'Edi', 'contactEmailAddress': None, 'primaryDomainName': 'yahoo', 'new_element': 'new_element_value'},
    {'loginName': 'Fabio', 'contactEmailAddress': 'edi@mail.com', 'primaryDomainName': 'google', 'new_element': None}]


@pytest.mark.skip
@pytest.mark.parametrize("update_args", update_args_input)
def test_update_data(update_args):
    logger.info(f"BEFORE: {data}")
    logger.info(f"AFTER: {update_data(data, **update_args)})")


@pytest.mark.skip
def test_token_1(get_eco_admin_access_token):
    # print('Test name: ' + inspect.currentframe().f_code.co_name)
    logger.info('eco_admin_access_token inside test: ' + get_eco_admin_access_token)
    assert 0


@pytest.mark.skip
def test_token_2(get_eco_admin_access_token):
    # print('Test name: ' + inspect.currentframe().f_code.co_name)
    logger.info('eco_admin_access_token inside test: ' + get_eco_admin_access_token)
    assert 0


# @pytest.mark.skip
@pytestrail.case('C12666499')
def test_credentials_2(user_credentials):
    assert 1 == 2


@pytest.mark.skip
# @pytestrail.case('C12666205')
def test_credentials_3(user_credentials):
    assert 1 == 1


class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):  # instance method
        # instance object accessible through self
        return "%s %s" % (self.name, self.surname)

    @classmethod
    def allowed_titles_starting_with(cls, startswith):  # class method
        # class or instance object accessible through cls
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith):  # static method
        # no parameter for class or instance object
        # we have to use Person directly
        return [t for t in Person.TITLES if t.endswith(endswith)]


class Employee(Person):
    def __init__(self, age, *args, **kwargs):
        self.age = age
        super().__init__(*args, **kwargs)

    # def fullname(self):
    #     print()


@pytest.mark.skip
def test_4():
    # jane = Person("Jane", "Smith")
    #
    # print(jane.fullname())
    #
    # print(jane.allowed_titles_starting_with("M"))
    # print(Person.allowed_titles_starting_with("M"))
    #
    # print(jane.allowed_titles_ending_with("s"))
    # print(Person.allowed_titles_ending_with("s"))

    bob_details = ['Bob', "Angel"]
    bob = Person(*bob_details)
    # logger = logging.getLogger()
    logger.error(f'Person full name is: {bob.fullname()}')
    # print(bob.fullname())

    edi = Employee('47', 'Edi', 'Gesyuk')
    logger.info(edi.__dict__)
