import json

from pynput import mouse


def on_click(x, y, button, pressed):
    print(f"click to:  x = {x} y = {y}")


def on_move(x, y):
    pass
    # print("Pointer moved to {0}".format((x, y)))


def on_scroll(x, y, dx, dy):
    pass
    # print("Scrolled {0} at {1}".format("down" if dy < 0 else "up", (x, y)))


def main():
    with mouse.Listener(
        on_move=on_move, on_scroll=on_scroll, on_click=on_click
    ) as listener:
        listener.join()
