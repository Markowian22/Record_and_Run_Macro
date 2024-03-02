from pynput import mouse


class RecordMouse:
    def __init__(self, controller) -> None:
        self.controller = controller

    def mouse_listener(self, select_method):
        if select_method == "click_at_position":
            self.controller.mouse_listener = mouse.Listener(on_click=self._on_click)

        elif select_method == "double_click_at_position":
            self.controller.mouse_listener = mouse.Listener(on_click=self._dobule_click)

        elif select_method == "move_to_position":
            self.controller.mouse_listener = mouse.Listener(
                on_click=self._move_to_position
            )

        self.controller.mouse_listener.start()
        self.controller.mouse_listener.join()

    def _on_click(self, x, y, button, pressed):
        if pressed:
            self.controller.steps["steps"].append(
                {"Click_at_position": {"coordinate_x": x, "coordinate_y": y}}
            )
        if self.controller.keyboard_listener is not None:
            self.controller.keyboard_listener.stop()
        self.controller.save_steps()
        return False

    def _dobule_click(self, x, y, button, pressed):
        if pressed:
            self.controller.steps["steps"].append(
                {"Double_click_at_position": {"coordinate_x": x, "coordinate_y": y}}
            )
        if self.controller.keyboard_listener is not None:
            self.controller.keyboard_listener.stop()
        self.controller.save_steps()
        return False

    def _move_to_position(self, x, y, button, pressed):
        if pressed:
            self.controller.steps["steps"].append(
                {"Move_to_position": {"coordinate_x": x, "coordinate_y": y}}
            )

        if self.controller.keyboard_listener is not None:
            self.controller.keyboard_listener.stop()

        self.controller.save_steps()
        return False
