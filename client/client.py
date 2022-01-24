"""
Implement a facade of the ReqRes API through a client class.
The client object will have the responsibility of constructing URLs, making requests and
providing functions that will be used from tests.
"""
import requests
from requests import Response
from hamcrest import is_, is_not


class ReqResClient:


    def __init__(self, url: str):
        self.url = url


    # Here we define all the API endpoints.
    # Endpoints are private as the consumer classes won't need to access urls directly.
    @property
    def __users_url(self) -> str:
        return f"{self.url}/users"

    @property
    def __login_url(self) -> str:
        return f"{self.url}/login"

    # Here we define all operations our API does, as python functions
    def get_users(self) -> Response:
        """Calls endpoint GET /users"""
        return requests.get(self.__users_url)

    def get_users_json(self):
        response = requests.get(self.__users_url)
        response_json = response.json()
        return response_json

    def post_user(self, name_str, job_str):
        """requires name and job"""
        request_body = {
            'name': name_str,
            'job': job_str
        }
        return requests.post(self.__users_url, data = request_body)

    def post_login(self, username, password):
        request_body = {
            'email': username,
            'password': password
        }
        return requests.post(self.__login_url, data = request_body)


# For each user retrieved verify URL inside the avatar property is a non empty string and a valid url

# When we call POST /api/users with a valid payload we should get a 201 response.
# Response should be well formed Json object that should contain the following fields:
# name, job, id, createdAt

# When we call POST /api/login using a payload with name but no password,
# we should get a 400 response. error should read "Missing password"

# When we call POST /api/login using a valid payload, we should get 200 response.
# The response object should contain the "token" property and its value should be a
# non-null and non-empty string
