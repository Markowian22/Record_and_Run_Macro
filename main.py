import typer

from recording_macro.record_controller import RecordController
from recording_macro.record_keyboard import RecordKeyboard
from recording_macro.record_mouse import RecordMouse
from running_macro.process import Process
from running_macro.run_controller import RunController


def main():
    FILE_NAME = "MACRO.json"

    app = typer.Typer()

    @app.command()
    def record_mouse_click_at_position():
        controller = RecordController(FILE_NAME)
        RecordMouse(controller).mouse_listener("click_at_position")

    @app.command()
    def record_mouse_double_click_at_position():
        controller = RecordController(FILE_NAME)
        RecordMouse(controller).mouse_listener("double_click_at_position")

    @app.command()
    def record_mouse_move_to_position():
        controller = RecordController(FILE_NAME)
        RecordMouse(controller).mouse_listener("move_to_position")

    @app.command()
    def record_key_press():
        controller = RecordController(FILE_NAME)
        RecordKeyboard(controller).keyboard_listener(select_method="on_press")

    @app.command()
    def record_hold_and_press():
        controller = RecordController(FILE_NAME)
        RecordKeyboard(controller).keyboard_listener(select_method="hold_and_press")

    @app.command()
    def record_type(text):
        controller = RecordController(FILE_NAME)
        RecordKeyboard(controller)._type(text)

    @app.command()
    def run_macro(file_name):
        controller = RunController()
        process = Process(file_name, controller=controller)
        process.load_steps()
        process.start()

    app()


if __name__ == "__main__":
    main()
