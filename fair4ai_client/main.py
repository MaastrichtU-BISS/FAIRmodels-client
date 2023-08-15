from typing import Dict, Any
from sklearn.base import BaseEstimator
from skl2onnx import convert_sklearn

from fair4ai_client.api import APIService

def wrap(model: BaseEstimator, sk2onnx_args: Dict[str, Any] = {}):
	onnx_obj = convert_sklearn(model, **sk2onnx_args)
	onnx_raw = onnx_obj.SerializeToString()
	process_onnx(onnx_raw)

def process_onnx(content):

    print("current api models:")
    api_service = APIService()
    api_service.list_models()

	# 1. ask user if instance already exists remotely (1), or if it should be treated as new (2)
    # 1.1. let user select instance
    # 1.2. ask user how to name new instance, among other information, and select instance
    # 2. upload ONNX-representation and link it to the selected instance
    
    print(f"** theoretically uploading: **")
    # print(content)

if __name__ == '__main__':
    print("This package should only be used as a package")