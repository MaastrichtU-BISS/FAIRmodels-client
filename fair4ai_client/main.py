import re
from typing import Dict, Any, List
from sklearn.base import BaseEstimator
from skl2onnx import convert_sklearn

from .menu import Menu

def wrap(model: BaseEstimator, sk2onnx_args: Dict[str, Any] = {}):
    onnx_obj = convert_sklearn(model, **sk2onnx_args)
    onnx_raw = onnx_obj.SerializeToString()
    
    menu = Menu()
    menu.model_entrypoint(onnx_raw)

menu = Menu()
menu.model_entrypoint("example-model-representation-2")

if __name__ == '__main__':
    print("This file should only be used as a package")