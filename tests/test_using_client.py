from hamcrest.core import assert_that
from hamcrest import is_, is_not

from client.client import ReqResClient


def test_users_return_200_and_not_empty_client(reqres_client: ReqResClient):
    """When we call GET /api/users we get 200 & non-empty data array"""
    response = reqres_client.get_users()
    assert_that(response.status_code, is_(200))
    assert_that(response.json(), is_not(None))


# For each user retrieved verify URL inside the avatar property is a non empty string and a valid url
def test_users_return_200_and_fields(reqres_client: ReqResClient):
    response = reqres_client.get_users()
    assert_that(response.status_code, is_(200))
    assert_that(reqres_client.avatar, is_not(None))

# When we call POST /api/users with a valid payload we should get a 201 response.
# Response should be well formed Json object that should contain the following fields:
# name, job, id, createdAt

# When we call POST /api/login using a payload with name but no password,
# we should get a 400 response. error should read "Missing password"

# When we call POST /api/login using a valid payload, we should get 200 response.
# The response object should contain the "token" property and its value should be a
# non-null and non-empty string
