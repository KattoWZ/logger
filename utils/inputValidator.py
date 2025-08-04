import time
from utils.uxHelper import clear_screen as clss
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError

class ReturnToMenu(Exception):
    pass
def reqInput(prompt):
    while True:
        value = input(prompt).strip()
        if value == "!":
            print("Returning to main menu.\n")
            time.sleep(0.5)
            clss()
            raise ReturnToMenu
        if value:
            return value
        else:
            print("!!!! This Field is REQUIRED. Please try again.")

def fancy_reqInput(message, choices=None, allow_return=True):
    completer = WordCompleter(choices, ignore_case=True) if choices else None

    def validate_text(text):
        if allow_return and text.strip() == "!":
            raise ReturnToMenu()
        if not text.strip():
            raise ValidationError(message="Input cannont be empty!")
        return True
    validator = Validator.from_callable(
        validate_text,
        error_message="Invalid Input.",
        move_cursor_to_end=True
    )

    try:
        return prompt(message, completer=completer, validator=validator)
    except ReturnToMenu:
        print("Returning to menu.")
        clss()
        raise


