import sys
import re
from typing import Dict, Any, List
from sklearn.base import BaseEstimator
from skl2onnx import convert_sklearn
from requests import exceptions

from .menu import Menu

def wrap_store(model: BaseEstimator, filename: str, sk2onnx_args: Dict[str, Any] = {}):
    onnx_obj = convert_sklearn(model, **sk2onnx_args)
    onnx_raw = onnx_obj.SerializeToString().hex()

    # if filename[-5] != '.onnx':
    filename += '.onnx'

    print("Welcome to FAIR4AI Model Wrapper")
    print()
    print_model_information(onnx_obj)
    print()
    try:
        with open(filename, 'w') as f:
            f.write(onnx_raw)
        print("File written to", filename)
    except:
        print("Can't write file")

def wrap(model: BaseEstimator, sk2onnx_args: Dict[str, Any] = {}):
    onnx_obj = convert_sklearn(model, **sk2onnx_args)
    onnx_raw = onnx_obj.SerializeToString().hex()

    print("Welcome to FAIR4AI Model Wrapper")
    print()
    print_model_information(onnx_obj)
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

def print_model_information(onnx_obj):
    print("Basic Model Information:\n")
    if onnx_obj.ir_version:
        print("> IR version:", onnx_obj.ir_version)
    if onnx_obj.producer_name:
        if onnx_obj.producer_version:
            print("> Producer:", onnx_obj.producer_name, f"(version {onnx_obj.producer_version})")
        else:
            print("> Producer:", onnx_obj.producer_name)
    if onnx_obj.doc_string:
        print("> Documentation string:", onnx_obj.doc_string)
    if onnx_obj.metadata_props:
        print("> Model metadata:", onnx_obj.doc_string)
        for metadata in onnx_obj.metadata_props:
            print("   - ", metadata)
    if onnx_obj.graph:
        print("> Graph node types:")
        for node in onnx_obj.graph.node:
            print(f"   - {node.name}")

if __name__ == '__main__':
    print("This file should be imported as a package")