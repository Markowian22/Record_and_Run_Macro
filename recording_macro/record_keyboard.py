from pynput import keyboard

from decorator import special_key_decorator


class RecordKeyboard:
    def __init__(self, controller) -> None:
        self.controller = controller
        self.key_to_hold = None

    def keyboard_listener(self, select_method):
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
        self.controller.steps["steps"].append({"click_button": {"button": f"{key}"}})
        if self.controller.mouse_listener is not None:
            self.controller.mouse_listener.stop()
        self.controller.save_steps()
        return False

    @special_key_decorator
    def _hold_and_press(self, key):
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
        self.controller.steps["steps"].append({"Type": {"text": text}})
        self.controller.save_steps()
