import typer

from recording_macro.record_controller import RecordController
from recording_macro.record_keyboard import RecordKeyboard
from recording_macro.record_mouse import RecordMouse
from running_macro.process import Process
from running_macro.run_controller import RunController


def main():
    """
    The main function of the program, which launches the user interface.
    """
    FILE_NAME = "MACRO.json"

    app = typer.Typer()

    @app.command()
    def record_mouse_click_at_position():
        """
        Records a mouse click and saves the step.
        """
        controller = RecordController(FILE_NAME)
        RecordMouse(controller).mouse_listener("Click_at_position")

    @app.command()
    def record_mouse_double_click_at_position():
        """
        Records a mouse double click and saves the step.
        """
        controller = RecordController(FILE_NAME)
        RecordMouse(controller).mouse_listener("Double_click_at_position")

    @app.command()
    def record_mouse_move_to_position():
        """
        Records a mouse movement and saves the step.
        """
        controller = RecordController(FILE_NAME)
        RecordMouse(controller).mouse_listener("Move_to_position")

    @app.command()
    def record_key_press():
        """
        Records a key press and saves the step.
        """
        controller = RecordController(FILE_NAME)
        RecordKeyboard(controller).keyboard_listener(select_method="on_press")

    @app.command()
    def record_hold_and_press():
        """
        Records a key hold and press and saves the step.
        """
        controller = RecordController(FILE_NAME)
        RecordKeyboard(controller).keyboard_listener(select_method="hold_and_press")

    @app.command()
    def record_type(text):
        """
        Records typing of text and saves the step.

        :param text: The text that was typed.
        :type text: str
        """
        controller = RecordController(FILE_NAME)
        RecordKeyboard(controller)._type(text)

    @app.command()
    def run_macro(file_name):
        """
        Runs a macro from the given file.

        :param file_name: The name of the file containing the macro to run.
        :type file_name: str
        """
        controller = RunController()
        process = Process(file_name, controller=controller)
        process.load_steps()
        process.start()

    app()


if __name__ == "__main__":
    main()
