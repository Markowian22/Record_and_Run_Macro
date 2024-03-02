import json
import os


class RecordController:
    """
    This class manages the process of recording user actions.
    """

    def __init__(self, file_name: str):
        """
        Initializes the controller with the given file name.

        :param file_name: The name of the file where the steps will be saved.
        :type file_name: str
        """
        self.file_name = file_name
        self.steps = {"steps": []}
        self.mouse_listener = None
        self.keyboard_listener = None

    def save_steps(self):
        """
        Saves the recorded steps to a JSON file.
        """
        if os.path.isfile(self.file_name):
            with open(self.file_name, "r") as file:
                data = json.load(file)
                data["steps"].extend(self.steps["steps"])
        else:
            data = self.steps

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)
