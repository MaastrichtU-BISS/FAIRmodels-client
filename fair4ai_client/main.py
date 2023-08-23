import sys
import re
from typing import Dict, Any, List
from sklearn.base import BaseEstimator
from skl2onnx import convert_sklearn
from requests import exceptions

from .menu import Menu

def wrap(model: BaseEstimator, sk2onnx_args: Dict[str, Any] = {}):
    onnx_obj = convert_sklearn(model, **sk2onnx_args)
    onnx_raw = onnx_obj.SerializeToString().hex()

    print("Welcome to FAIR4AI Model Wrapper")
    print()
    print("Basic Model Information:\n")
    print("- Node types:")
    for node in onnx_obj.graph.node:
        print(f"  - {node.name}")
    print()
    
    try:
        menu = Menu()
        menu.model_entrypoint(onnx_raw)
    except KeyboardInterrupt:
        print("Quiting...")
        sys.exit()
    except exceptions.ConnectionError:
        print("Failed connecting to the server. Exiting...")
        sys.exit()

if __name__ == '__main__':
    print("This file should be imported as a package")