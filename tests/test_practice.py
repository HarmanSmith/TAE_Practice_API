import requests
import validators
from hamcrest.core import assert_that
from hamcrest import is_, is_not


# When we call GET /api/users we get 200 & non-empty data array
def test_users_return_200_and_not_empty(config):
    """Only checks if something has been received"""
    response = requests.get(config['url'] + "/users")
    assert_that(response.status_code, is_(200))
    assert_that(response.json(), is_not(None))


# When we call GET /api/users we get 200 &
# verify all users for containing id, email, first_name, last_name, avatar
def test_users_return_200_and_fields(config):
    """Checking that every field is populated,
    the actual contents are not checked"""
    response = requests.get(config['url']+"/users")
    assert_that(response.status_code, is_(200))
    response_obj = response.json()
    for user_index in response_obj['data']:
        assert_that(user_index['id'], is_not(None))
        assert_that(user_index['email'], is_not(None))
        assert_that(user_index['first_name'], is_not(None))
        assert_that(user_index['last_name'], is_not(None))
        assert_that(user_index['avatar'], is_not(None))


# When we call GET /api/users, we should get a 200 response.
# For each user retrieved verify URL inside the avatar property is a non empty string and a valid url
def test_users_return_200_and_avatar_url(config):
    """We use the validators package for handling the URL"""
    response = requests.get(config['url'] + "/users")
    assert_that(response.status_code, is_(200))
    response_obj = response.json()
    for user_index in response_obj['data']:
        assert_that(user_index['avatar'], is_not(None))
        assert_that(validators.url(user_index['avatar']))


# When we call POST /api/users with a valid payload we should get a 201 response.
# Response should be well formed Json object that should contain the following fields:
# name, job, id, createdAt
def test_create_user_successful(config):
    """We post to create a new user and check the response."""
    request_body = {
        'name': 'Erdrick',
        'job': 'Hero'
    }
    response = requests.post(config['url'] + "/users", data=request_body)
    assert_that(response.status_code, is_(201))
    response_obj = response.json()
    assert_that(response_obj['name'], is_('Erdrick'))
    assert_that(response_obj['job'], is_('Hero'))
    assert_that(response_obj['id'], is_not(None))
    assert_that(response_obj['createdAt'], is_not(None))


# When we call POST /api/login using a payload with name but no password,
# we should get a 400 response. error should read "Missing password"
def test_login_no_password(config):
    """login data taken from https://reqres.in/"""
    request_body = {
        'email': 'eve.holt@reqres.in',
        'password': None
    }
    response = requests.post(config['url'] + "/login", data=request_body)
    assert_that(response.status_code, is_(400))
    response_obj = response.json()
    assert_that(response_obj['error'], is_('Missing password'))

# When we call POST /api/login using a valid payload, we should get 200 response.
# The response object should contain the "token" property and its value should be a
# non-null and non-empty string
def test_login_valid(config):
    """login information taken from https://reqres.in/"""
    request_body = {
        'email': 'eve.holt@reqres.in',
        'password': 'cityslicka'
    }
    response = requests.post(config['url'] + "/login", data=request_body)
    assert_that(response.status_code, is_(200))
    response_obj = response.json()
    assert_that(response_obj['token'], is_not(None))
    assert_that(response_obj['token'], is_not(''))
