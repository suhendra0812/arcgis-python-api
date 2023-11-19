from dataclasses import dataclass, field
from urllib.parse import urlparse

import requests


@dataclass
class Auth:
    token_url: str = field(init=False, repr=False)
    portal_url: str
    username: str
    password: str = field(repr=False)

    def __post_init__(self) -> None:
        parsed_url = urlparse(self.portal_url)
        scheme = parsed_url.scheme
        domain = parsed_url.netloc
        self.token_url = f"{scheme}://{domain}/arcgis/sharing/rest/generateToken"

    def get_token(self) -> str:
        data = {
            "username": self.username,
            "password": self.password,
            "referer": self.portal_url,
            "f": "json",
        }
        response = requests.post(self.token_url, data=data)
        return response.json()["token"]
