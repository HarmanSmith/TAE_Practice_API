from hamcrest.core import assert_that
from hamcrest import is_, is_not

from client.client import ReqResClient


def test_users_return_200_and_not_empty_client(reqres_client: ReqResClient):
    """When we call GET /api/users we get 200 & non-empty data array"""
    response = reqres_client.get_users()
    assert_that(response.status_code, is_(200))
    assert_that(response.json(), is_not(None))
