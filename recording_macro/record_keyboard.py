from pynput import keyboard

from decorator import special_key_decorator


class RecordKeyboard:
    """
    This class listens for and records keyboard actions.
    """

    def __init__(self, controller) -> None:
        """
        Initializes the object with the given controller.

        :param controller: The controller that manages the recording process.
        :type controller: RecordController
        """
        self.controller = controller
        self.key_to_hold = None

    def keyboard_listener(self, select_method):
        """
        Starts listening for keyboard events based on the selected method.

        :param select_method: The method of listening, either "on_press" or "hold_and_press".
        :type select_method: str
        """
        if select_method == "on_press":
            self.controller.keyboard_listener = keyboard.Listener(
                on_press=self._on_press
            )
        elif select_method == "hold_and_press":
            self.controller.keyboard_listener = keyboard.Listener(
                on_press=self._hold_and_press
            )

        self.controller.keyboard_listener.start()
        self.controller.keyboard_listener.join()

    @special_key_decorator
    def _on_press(self, key):
        """
        Records a key press and saves the step.

        :param key: The key that was pressed.
        :type key: pynput.keyboard.Key or pynput.keyboard.KeyCode
        """
        self.controller.steps["steps"].append({"click_button": {"button": f"{key}"}})
        if self.controller.mouse_listener is not None:
            self.controller.mouse_listener.stop()
        self.controller.save_steps()
        return False

    @special_key_decorator
    def _hold_and_press(self, key):
        """
        Records a key hold and press and saves the step.

        :param key: The key that was pressed while another key was held.
        :type key: pynput.keyboard.Key or pynput.keyboard.KeyCode
        """
        if self.key_to_hold is None:
            self.key_to_hold = key
        else:
            self.controller.steps["steps"].append(
                {
                    "Hold_and_press": {
                        "button_to_hold": f"{self.key_to_hold}",
                        "button_to_press": f"{key}",
                    }
                }
            )
            if self.controller.mouse_listener is not None:
                self.controller.mouse_listener.stop()
            self.controller.save_steps()
            print(f"""button_to_hold:" {self.key_to_hold}\n"button_to_press: {key}""")
            return False

    def _type(self, text):
        """
        Records typing of text and saves the step.

        :param text: The text that was typed.
        :type text: str
        """
        self.controller.steps["steps"].append({"Type": {"text": text}})
        self.controller.save_steps()
