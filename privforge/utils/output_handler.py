from typing import Any
from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

def output_handler(
    is_error: bool = False,
    message: str = "",
    error_detail: Any = None,
    with_panel: bool = False,
    title: str = "",
    border_style: str = "",
    box=box.ROUNDED,
) -> None:

    error_d = error_detail or ""

    if is_error:

        console.print(f"\n[bold red][!] {message} [/bold red] {error_d}")
        assert False, 'Error trigged ... !'

    elif with_panel:

        console.print(
            Panel.fit(
                message,
                title=title,
                box=box,
                border_style=border_style,
            )
        )

    else:
        console.print(message)
