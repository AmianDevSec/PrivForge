from rich.table import Table
from rich import box
import Utils.output_handler as oh

functions = [
    "shell",
    "command",
    "reverse-shell",
    "non-interactive-reverse-shell",
    "bind-shell",
    "non-interactive-bind-shell",
    "file-upload",
    "file-download",
    "file-write",
    "file-read",
    "library-load",
    "suid",
    "sudo",
    "capabilities",
    "limited-suid",
]

def show_functions():
    table = Table(box=box.MINIMAL_DOUBLE_HEAD)  # title="Available Functions",
    table.add_column("Available Functions", style="bold cyan", justify="left")

    for f in functions:
        table.add_row(f)

    oh.output_handler(message=table)
