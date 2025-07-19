from typing import Any
from rich.prompt import Prompt, Confirm
from privforge.utils.formatter import (
    RESET,
    BLUE,
)

def user_input(choices: list = None, label: str = "", default: str = None) ->Any:
    prompt = Prompt.ask(f"{BLUE}{label}{RESET}", choices=choices, default=default)
    return prompt

def confirm_input(label: str)-> Any:
    is_confirmed = Confirm.ask(f"{BLUE}{label}{RESET}")
    # assert is_confirmed

    return is_confirmed
