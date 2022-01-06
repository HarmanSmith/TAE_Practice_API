import requests
from hamcrest.core import assert_that
from hamcrest import is_, is_not

def test_users_return_200_and_not_empty(config):
    response = requests.get(config['url'] + "/users")
    assert_that(response.status_code, is_(200))
    assert_that(response.json(), is_not(None))


def test_create_user_successful(config):
    request_body = {
        'name': 'Hal Emmerich',
        'job': 'Programmer'
    }
    response = requests.post(config['url'] + "/users", data=request_body)
    assert_that(response.status_code, is_(201))

    response_obj = response.json()
    assert_that(response_obj['name'], is_('Snake Plisskin'))
    assert_that(response_obj['job'], is_not('Philantropist'))