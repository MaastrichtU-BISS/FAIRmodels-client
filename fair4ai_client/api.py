import sys
from typing import TypedDict
import requests

from fair4ai_client.utils.input import read_pattern_input

TOKEN_FILE_PATH = '~/.fair4ai/token'
PATTERN_EMAIL = r'^.+\@(.+\..+|localhost)$'
PATTERN_PASSWORD = r'^.+$'


class APIService:
    base_url = 'http://localhost:8000'
    session = requests.Session()
    
    def __init__(self, ):
        self.login()
        # self.auth = AuthService(self.session)
    
    def login(self):
        # new procedure:
        # 1. user generates API token on backend login page
        # 2. user copies token
        # 3. client checks if token exists in home folder, else asks
        # ^ according to https://florimondmanca.github.io/djangorestframework-api-key/security/
        # ^ using apikeys is often not recommended

        # new new strategy:
        #   JWT authentication, storing the access- and refreshtokens in keyring. 
        #   Using a requests session with an authorization header and hooks
        #   for detecting out-of-date access-tokens (https://stackoverflow.com/a/69226185/17864167)

        print("Enter your credentials below\n")
        print("  Enter your email:")
        email = read_pattern_input(pattern=PATTERN_EMAIL)
        print("  Enter your password:")
        password = read_pattern_input(pattern=PATTERN_PASSWORD)
        
        response = requests.post(
            f"{APIService.base_url}/auth/login/",
            json={"email": email, "password": password},
            verify=False
        )

        resp_json = response.json()

        if response.status_code // 100 == 2 and resp_json["access"] and resp_json["refresh"]:
            print("Login successful")

        elif response.status_code // 100 == 5:
            print("An internal server error occured. Please try again later.")
            sys.exit()
        elif response.status_code // 100 == 4:
            error_types = [
                ["email", "There are one or more errors with your email"],
                ["password", "There are one or more errors with your password"],
                ["non_field_errors", "There are one more errors with your details:"],
            ]

            resp_json = response.json()
            
            print()
            for error_type in error_types:
                if error_type[0] in resp_json and resp_json[error_type[0]] is not None:
                    print(f" {error_type[1]}:")
                    for error in resp_json[error_type[0]]:
                        print(f"  - {error}")
            
            print("\nPlease try again\n")
            self.login()

        pass

    def list_models(self):
        url = f"{self.base_url}/model"
        response = self.session.get(url)
        return response.json()
    
    def create_model(self, data):
        url = f"{self.base_url}/model"
        response = self.session.post(url, json=data)
        return response.json()
    
    def read_model(self, model_id):
        url = f"{self.base_url}/model/{model_id}"
        response = self.session.get(url)
        return response.json()
    
    def update_model(self, model_id, onnx_model: str, update_type: str, update_description: str):
        url = f"{self.base_url}/model/{model_id}"
        response = self.session.patch(url, json={
            "onnx_model": onnx_model,
            "update_type": update_type,
            "update_description": update_description
        })
        return response.json()
    
    def delete_model(self, model_id):
        url = f"{self.base_url}/model/{model_id}"
        response = self.session.delete(url)
        return response.json()