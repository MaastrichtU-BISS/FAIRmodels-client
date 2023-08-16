from typing import List
from api import APIService

def read_input(prefix="> ", valid: List[str] = []):
    value = input(prefix).rstrip()
    while not value in map(str, valid):
        value = input(prefix).rstrip()
    return value

def process_menu_create(onnx_model):
    pass

def process_menu_update(id, onnx_model):
    pass

def process_menu_entrypoint(onnx_model):

	# 1. ask user if instance already exists remotely (1.1), or if it should be treated as new (1.2)
    # 1.1. let user select instance
    # 1.2. ask user how to name new instance, among other information, and select instance
    # 2. upload ONNX-representation and link it to the selected instance

    print()
    print("Available models:")
    print()

    api_service = APIService()
    models = api_service.list_models()
    model_ids = list(models.keys())

    idmap = {i + 1: model_ids[i] for i in range(len(model_ids))}

    for (i, id) in idmap.items():
        print(f"- {i}) {models[id]['name']}")

    print("\n- N) New model")
    print("\n- A) Abort")
    print("")
    print("Is this model present in this list, or is this a new model?")

    model_number = read_input(valid=[*range(1, len(idmap)+1), 'N', 'n', 'A', 'a'])

    if model_number in ['N', 'n']:
        process_model_create()
    elif model_number in ['A', 'a']:
        print("Aborting...")
        return
    else:
        process_model_update()

