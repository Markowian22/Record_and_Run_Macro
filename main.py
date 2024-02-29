import typer

# from run_app import Process, RunController
from recording_macro.record_controller import RecordController
from recording_macro.record_keyboard import RecordKeyboard
from recording_macro.record_mouse import RecordMouse
from running_macro.process import Process
from running_macro.run_controller import RunController

# def main():


def main():
    app = typer.Typer()

    @app.command()
    def record_mouse():
        controller = RecordController()
        RecordMouse(controller).mouse_listener()

    @app.command()
    def record_key_press():
        controller = RecordController()
        RecordKeyboard(controller).keyboard_listener(select_method="on_press")

    @app.command()
    def record_hold_and_press():
        controller = RecordController()
        RecordKeyboard(controller).keyboard_listener(select_method="hold_and_press")

    @app.command()
    def record_type(text):
        controller = RecordController()
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
