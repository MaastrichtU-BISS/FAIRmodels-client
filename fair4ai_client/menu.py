import re
from typing import List
from api import APIService

def read_choice_input(prefix="# ", valid: List[str] = [], case_upper=True):
    value = input(prefix)
    if case_upper: value = value.upper()
    while not value in map(str, valid):
        value = input(prefix)
        if case_upper: value = value.upper()
    return value

def read_pattern_input(prefix="> ", pattern: re.Pattern = r'.+', flags: re.RegexFlag = 0):
    value = input(prefix)
    while not re.match(pattern, value, flags):
        value = input(prefix)
    return value

class Menu:
    def __init__(self) -> None:
        self.api = APIService()

    def model_create(self, onnx_model):

        print("\n- Name:")
        in_name = read_pattern_input()

        print("\n- Description:")
        in_desc = read_pattern_input(pattern=r'.*')

        print("\nUploading model...")
        model_resp = self.api.create_model({
            "name": in_name,
            "version": "0.1.0",
            "description": in_desc,
            "onnx_model": onnx_model,
        })
        print(f"Model uploaded with ID '{ model_resp['id'] }'")

    def model_update(self, model_id, onnx_model):

        print("\n- Is this update change a [ma]jor, a [mi]nor, or a [p]atch?")
        in_update_type = read_pattern_input('# ', r'^(ma|maj|majo|major|mi|min|mino|minor|p|pa|pat|patc|patch)$', re.IGNORECASE).lower()
        update_type = None
        if in_update_type.startswith('mi'):
            update_type = 'minor'
        elif in_update_type.startswith('ma'):
            update_type = 'major'
        elif in_update_type.startswith('p'):
            update_type = 'patch'

        if update_type is None:
            raise Exception(f"Invalid version-type '{in_update_type}'")
        
        print("\n- Description for this update:")
        in_update_description = read_pattern_input()

        print("\nUpdating model...")
        response = self.api.update_model(model_id, onnx_model, update_type, in_update_description)
        print(f"Model with ID '{ model_id }' updated. New version: {response['version']}")

    def model_entrypoint(self, onnx_model):

      # 1. ask user if instance already exists remotely (1.1), or if it should be treated as new (1.2)
        # 1.1. let user select instance
        # 1.2. ask user how to name new instance, among other information, and select instance
        # 2. upload ONNX-representation and link it to the selected instance

        models = self.api.list_models()
        model_ids = list(models.keys())

        idmap = {i + 1: model_ids[i] for i in range(len(model_ids))}

        if len(model_ids) > 0:
            print()
            print("Available models:")
            print()

            for (i, id) in idmap.items():
                print(f"- {i}) {models[id]['name']}")
        else:
            print("\n No models available yet.")

        print()
        print("- N) Create new model")
        print("- A) Abort")
        print()
        print("Is this model present in this list, or is this a new model?")
        print()

        choice = read_choice_input(valid=[*range(1, len(idmap)+1), 'N', 'A'])

        if choice in ['N']:
            self.model_create(onnx_model)
        elif choice in ['A']:
            print("Aborting...")
            return
        else:
            self.model_update(idmap[int(choice)], onnx_model)

