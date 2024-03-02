import json

from pynput.keyboard import Key, KeyCode


class Process:
    """
    This class is responsible for loading and executing a series of steps from a file.
    """

    def __init__(self, filename: str, controller):
        """
        Initializes the `Process` instance with the given filename and controller.

        :param filename: The name of the file where the steps are stored.
        :type filename: str
        :param controller: The controller that manages the execution process.
        :type controller: RunController
        """
        self.filename = filename
        self.steps = []
        self.controller = controller

    def load_steps(self):
        """
        Loads the steps from the file specified in the filename.
        """
        with open(self.filename, "r") as file:
            self.steps = json.load(file)["steps"]

    def start(self):
        """
        Executes the loaded steps. The steps are a series of actions that are executed using the controller.
        """
        options = {
            "Type": self.controller.keyboard.type,
            "Click_button": lambda button: self.controller.keyboard.click_button(
                KeyCode.from_char(button) if len(button) == 1 else getattr(Key, button)
            ),
            "Hold_and_press": lambda button_to_hold,
            button_to_press: self.controller.keyboard.hold_and_press(
                KeyCode.from_char(button_to_hold)
                if len(button_to_hold) == 1
                else getattr(Key, button_to_hold),
                KeyCode.from_char(button_to_press)
                if len(button_to_press) == 1
                else getattr(Key, button_to_press),
            ),
            "Click_at_position": self.controller.mouse.click_at_position,
            "Double_click_at_position": self.controller.mouse.double_click_at_position,
            "Move_to_position": self.controller.mouse.move_to_position,
        }

        for step in self.steps:
            for key, value in step.items():
                options[key](**value)
