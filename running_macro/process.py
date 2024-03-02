import json

from pynput.keyboard import Key


class Process:
    def __init__(self, filename, controller):
        self.filename = filename
        self.steps = []
        self.controller = controller

    def load_steps(self):
        with open(self.filename, "r") as file:
            self.steps = json.load(file)["steps"]

    def start(self):
        options = {
            "Type": self.controller.keyboard.type,
            "Click_button": lambda button: self.controller.keyboard.click_button(
                getattr(Key, button)
            ),
            "Hold_and_press": lambda button_to_hold,
            button_to_press: self.controller.keyboard.hold_and_press(
                getattr(Key, button_to_hold), getattr(Key, button_to_press)
            ),
            "Click_at_position": self.controller.mouse.click_at_position,
            "Double_click_at_position": self.controller.mouse.double_click_at_position,
            "Move_to_position": self.controller.mouse.move_to_position,
        }

        for step in self.steps:
            for key, value in step.items():
                options[key](**value)
