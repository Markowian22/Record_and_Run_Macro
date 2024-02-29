import json
import os


class RecordController:
    def __init__(self):
        self.steps = {"steps": []}
        self.mouse_listener = None
        self.keyboard_listener = None

    def save_steps(self):
        if os.path.isfile("test.json"):
            with open("test.json", "r") as file:
                data = json.load(file)
                data["steps"].extend(self.steps["steps"])
        else:
            data = self.steps

        with open("test.json", "w") as file:
            json.dump(data, file, indent=4)
