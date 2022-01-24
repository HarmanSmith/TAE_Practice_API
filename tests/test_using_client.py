import validators
from hamcrest.core import assert_that
from hamcrest import is_, is_not

from client.client import ReqResClient


def test_users_return_200_and_not_empty_client(reqres_client: ReqResClient):
    """When we call GET /api/users we get 200 & non-empty data array"""
    response = reqres_client.get_users()
    assert_that(response.status_code, is_(200))
    assert_that(response.json(), is_not(None))


def test_users_return_200_and_fields(reqres_client: ReqResClient):
    response = reqres_client.get_users()
    response_json = response.json()
    assert_that(response.status_code, is_(200))
    for user_index in response_json['data']:
        assert_that(user_index['id'], is_not(None))
        assert_that(user_index['email'], is_not(None))
        assert_that(user_index['first_name'], is_not(None))
        assert_that(user_index['last_name'], is_not(None))
        assert_that(user_index['avatar'], is_not(None))


# For each user retrieved verify URL inside the avatar property is a non empty string and a valid url
def test_users_avatar(reqres_client: ReqResClient):
    response = reqres_client.get_users()
    response_json = response.json()
    assert_that(response.status_code, is_(200))
    for user_index in response_json['data']:
        assert_that(user_index['avatar'], is_not(None))
        assert_that(validators.url(user_index['avatar']))

# When we call POST /api/users with a valid payload we should get a 201 response.
# Response should be well formed Json object that should contain the following fields:
# name, job, id, createdAt
def test_create_user_successful(reqres_client: ReqResClient):
    response = reqres_client.post_user("Rob","Writer")
    assert_that(response.status_code, is_(201))
    response_json = response.json()
    assert_that(response_json['name'], is_('Rob'))
    assert_that(response_json['job'], is_('Writer'))
    assert_that(response_json['id'], is_not(None))
    assert_that(response_json['createdAt'], is_not(None))


# When we call POST /api/login using a payload with name but no password,
# we should get a 400 response. error should read "Missing password"
def test_login_no_password(reqres_client: ReqResClient):
    """login data taken from https://reqres.in/"""
    response = reqres_client.post_login("eve.holt@reqres.in", None)
    assert_that(response.status_code, is_(400))
    response_json = response.json()
    assert_that(response_json['error'], is_('Missing password'))


# When we call POST /api/login using a valid payload, we should get 200 response.
# The response object should contain the "token" property and its value should be a
# non-null and non-empty string
def test_login_correct(reqres_client: ReqResClient):
    """login data taken from https://reqres.in/"""
    response = reqres_client.post_login("eve.holt@reqres.in", "cityslicka")
    assert_that(response.status_code, is_(200))
    response_json = response.json()
    assert_that(response_json['token'], is_not(None))
    assert_that(response_json['token'], is_not(''))
