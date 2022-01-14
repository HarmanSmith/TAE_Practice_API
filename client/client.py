"""
Implement a facade of the ReqRes API through a client class.
The client object will have the responsibility of constructing URLs, making requests and
providing functions that will be used from tests.
"""
import requests
from requests import Response


class ReqResClient:
    def __init__(self, url: str):
        self.url = url

    # Here we define all the API endpoints.
    # Endpoints are private as the consumer classes won't need to access urls directly.
    @property
    def __users_url(self) -> str:
        return f"{self.url}/users"

    # Here we define all operations our API does, as python functions
    def get_users(self) -> Response:
        """Calls endpoint GET /users"""
        return requests.get(self.__users_url)
