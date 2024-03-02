from time import sleep

from pynput import keyboard, mouse
from pynput.mouse import Button

from decorator import delay


class RunController:
    """
    This class is a controller that manages the execution of keyboard and mouse actions.
    """

    def __init__(self) -> None:
        """
        Initializes the `RunController` instance and creates instances of `MouseController` and `KeyboardController`.
        """
        self.mouse = self.MouseController()
        self.keyboard = self.KeyboardController()

    class KeyboardController:
        """
        This class is responsible for executing keyboard actions.
        """

        def __init__(self):
            """
            Initializes the `KeyboardController` instance.
            """
            self.keyboard = keyboard.Controller()

        @delay(1)
        def click_button(self, button):
            """
            Simulates a button click.

            :param button: The button to click.
            :type button: pynput.keyboard.Key or pynput.keyboard.KeyCode
            """
            self.keyboard.press(button)
            self.keyboard.release(button)

        @delay(1)
        def type(self, text: str):
            """
            Simulates typing a string of text.

            :param text: The text to type.
            :type text: str
            """
            self.keyboard.type(text)

        @delay(0.5)
        def hold_and_press(self, button_to_hold, button_to_press):
            """
            Simulates holding one button while pressing another.

            :param button_to_hold: The button to hold.
            :type button_to_hold: pynput.keyboard.Key or pynput.keyboard.KeyCode
            :param button_to_press: The button to press while holding the other button.
            :type button_to_press: pynput.keyboard.Key or pynput.keyboard.KeyCode
            """
            with self.keyboard.pressed(button_to_hold):
                self.keyboard.press(button_to_press)
                self.keyboard.release(button_to_press)

    class MouseController:
        """
        This class is responsible for executing mouse actions.
        """

        def __init__(self):
            """
            Initializes the `MouseController` instance.
            """
            self.mouse = mouse.Controller()

        @delay(1)
        def move_to_position(self, coordinate_x: float, coordinate_y: float):
            """
            Moves the mouse to the specified coordinates.

            :param coordinate_x: The x-coordinate to move the mouse to.
            :type coordinate_x: float
            :param coordinate_y: The y-coordinate to move the mouse to.
            :type coordinate_y: float
            """
            self.mouse.position = (coordinate_x, coordinate_y)

        @delay(1)
        def click_at_position(
            self, coordinate_x: float, coordinate_y: float, button=Button.left
        ):
            """
            Moves the mouse to the specified coordinates and simulates a mouse click.

            :param coordinate_x: The x-coordinate to move the mouse to.
            :type coordinate_x: float
            :param coordinate_y: The y-coordinate to move the mouse to.
            :type coordinate_y: float
            :param button: The button to click.
            :type button: pynput.mouse.Button
            """
            self.mouse.position = (coordinate_x, coordinate_y)
            sleep(0.5)
            self.mouse.click(button, 1)

        @delay(1)
        def double_click_at_position(
            self, coordinate_x: float, coordinate_y: float, button=Button.left
        ):
            """
            Moves the mouse to the specified coordinates and simulates a double mouse click.

            :param coordinate_x: The x-coordinate to move the mouse to.
            :type coordinate_x: float
            :param coordinate_y: The y-coordinate to move the mouse to.
            :type coordinate_y: float
            :param button: The button to double click.
            :type button: pynput.mouse.Button
            """
            self.mouse.position = (coordinate_x, coordinate_y)
            sleep(1)
            self.mouse.click(button, 2)

        @delay(1)
        def press_mouse_button(self, button=Button.left):
            """
            Simulates pressing a mouse button.

            :param button: The button to press.
            :type button: pynput.mouse.Button
            """
            self.mouse.press(button)

        @delay(1)
        def release_mouse_button(self, button=Button.left):
            """
            Simulates releasing a mouse button.

            :param button: The button to release.
            :type button: pynput.mouse.Button
            """
            self.mouse.release(button)

        @delay(1)
        def move_pointer(self, dx: float = 0, dy: float = 0):
            """
            Moves the mouse pointer by the specified amounts in the x and y directions.

            :param dx: The amount to move the mouse in the x direction.
            :type dx: float
            :param dy: The amount to move the mouse in the y direction.
            :type dy: float
            """
            self.mouse.move(dx=dx, dy=dy)
