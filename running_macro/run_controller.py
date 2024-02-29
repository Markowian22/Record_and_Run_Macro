from time import sleep

from decorator import delay
from pynput import keyboard, mouse
from pynput.mouse import Button


class RunController:
    def __init__(self) -> None:
        self.mouse = self.MouseController()
        self.keyboard = self.KeyboardController()

    class KeyboardController:
        def __init__(self):
            self.keyboard = keyboard.Controller()

        @delay(1)
        def click_button(self, button):
            self.keyboard.press(button)
            self.keyboard.release(button)

        @delay(1)
        def type(self, text):
            self.keyboard.type(text)

        @delay(0.5)
        def hold_and_press(self, button_to_hold, button_to_press):
            with self.keyboard.pressed(button_to_hold):
                self.keyboard.press(button_to_press)
                self.keyboard.release(button_to_press)

    class MouseController:
        def __init__(self):
            self.mouse = mouse.Controller()

        @delay(1)
        def move_to_position(self, coordinate_x, coordinate_y):
            self.mouse.position = (coordinate_x, coordinate_y)

        @delay(1)
        def click_at_position(self, coordinate_x, coordinate_y, button=Button.left):
            self.mouse.position = (coordinate_x, coordinate_y)
            sleep(0.5)
            self.mouse.click(button, 1)

        @delay(1)
        def press_mouse_button(self, button=Button.left):
            self.mouse.press(button)

        @delay(1)
        def release_mouse_button(self, button=Button.left):
            self.mouse.release(button)

        @delay(1)
        def move_pointer(self, dx=0, dy=0):
            self.mouse.move(dx=dx, dy=dy)
