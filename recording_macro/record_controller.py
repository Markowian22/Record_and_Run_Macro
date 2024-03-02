import json
import os


class RecordController:
    def __init__(self, file_name):
        self.file_name = file_name
        self.steps = {"steps": []}
        self.mouse_listener = None
        self.keyboard_listener = None

    def save_steps(self):
        if os.path.isfile(self.file_name):
            with open(self.file_name, "r") as file:
                data = json.load(file)
                data["steps"].extend(self.steps["steps"])
        else:
            data = self.steps

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)
