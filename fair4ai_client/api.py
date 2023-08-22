import requests

class APIService:
    def __init__(self, base_url = 'http://localhost:3099'):
        self.base_url = base_url

    def list_models(self):
        url = f"{self.base_url}/model"
        response = requests.get(url)
        return response.json()
    
    def create_model(self, data):
        url = f"{self.base_url}/model"
        response = requests.post(url, json=data)
        return response.json()
    
    def read_model(self, model_id):
        url = f"{self.base_url}/model/{model_id}"
        response = requests.get(url)
        return response.json()
    
    def update_model(self, model_id, onnx_model: str, update_type: str, update_description: str):
        url = f"{self.base_url}/model/{model_id}"
        response = requests.patch(url, json={
            "onnx_model": onnx_model,
            "update_type": update_type,
            "update_description": update_description
        })
        return response.json()
    
    def delete_model(self, model_id):
        url = f"{self.base_url}/model/{model_id}"
        response = requests.delete(url)
        return response.json()