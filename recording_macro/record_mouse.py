from pynput import mouse

from recording_macro.record_controller import RecordController


class RecordMouse:
    """
    This class listens for and records mouse actions.
    """

    def __init__(self, controller: RecordController) -> None:
        """
        Initializes the object with the given controller.

        :param controller: The controller that manages the recording process.
        :type controller: RecordController
        """
        self.controller = controller

    def mouse_listener(self, action_type: str):
        """
        Starts listening for mouse events based on the selected action type.

        :param action_type: The type of the mouse action. Can be "Click_at_position", "Double_click_at_position", or "Move_to_position".
        :type action_type: str
        """
        self.controller.mouse_listener = mouse.Listener(
            on_click=lambda x, y, button, pressed: self._record_action(
                x, y, button, pressed, action_type
            )
        )
        self.controller.mouse_listener.start()
        self.controller.mouse_listener.join()

    def _record_action(self, x, y, button, pressed, action_type: str):
        """
        Records a mouse action and saves the step.

        :param x: The x-coordinate of the mouse action.
        :type x: float
        :param y: The y-coordinate of the mouse action.
        :type y: float
        :param button: The button that was clicked.
        :type button: pynput.mouse.Button
        :param pressed: Whether the button was pressed.
        :type pressed: bool
        :param action_type: The type of the mouse action. Can be "Click_at_position", "Double_click_at_position", or "Move_to_position".
        :type action_type: str
        """
        if pressed:
            self.controller.steps["steps"].append(
                {action_type: {"coordinate_x": x, "coordinate_y": y}}
            )

        if self.controller.keyboard_listener is not None:
            self.controller.keyboard_listener.stop()

        self.controller.save_steps()
        return False
