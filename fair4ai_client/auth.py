import requests

class AuthService:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self):
        # 1. check if token is stored from previous session (file in home folder), else:
        # 2. request validation link from /api/request_challenge
        # 3. * user clicks on link, and signs in on the website and copies response code *
        # 4. * user pastes respones code in terminal and presses enter *
        # 5. request token using [challenge, code] from /api/request_token
        pass

    def refresh_token(self):
        pass

    def logout(self):
        # if session file in home folder, release file