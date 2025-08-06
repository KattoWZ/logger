import time
from utils.uxHelper import clear_screen as clss
from pathlib import Path
from prompt_toolkit import prompt, PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError

class ReturnToMenu(Exception):
    pass
def XreqInput(prompt):
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

#for general usage
def reqInput(message, choices=None, allow_return=True):
    session = PromptSession()
    completer = WordCompleter(choices, ignore_case=True) if choices else None


    class InputValidator(Validator):
        def validate(self, document):
            text = document.text.strip()

            if text == "!":
                return
            
            if not text:
                raise ValidationError(message="This field can't be empty!!!!" , cursor_position=0)

    text = session.prompt(
        message,
        completer=completer,
        validator=InputValidator(),
        validate_while_typing=False
        
    )


    if allow_return and text == "!":
        clss()
        print("\nReturning to main menu...")
        raise ReturnToMenu()
    return text

#for Inputing Filename

def input_filename(message, path:Path, allow_return=True):
    session = PromptSession()

    json_files = [f.name for f in path.glob("*.json")]
    completer = WordCompleter(json_files, ignore_case=True)

    class FileNameValidator(Validator):
        def validate(self, document):
            text = document.text.strip()

            if text == "!":
                return
            if not text:
                raise ValidationError(message="Filename can't be empty!", cursor_position=0)

    filename = session.prompt(
        message,
        completer=completer,
        validator=FileNameValidator(),
        validate_while_typing=False
    ).strip()

    if allow_return and filename == "!":
        clss()
        print("\nReturning to main menu...")
        raise ReturnToMenu()

    return filename
