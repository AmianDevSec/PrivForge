from pathlib import Path
import json
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
import Utils.output_handler as oh
import Utils.path_handler as ph

console = Console()

def search_binary(binary: str, func: str) -> str | None:

    # oh.output_handler(is_error=True, message="Are u crazy ?!")
    try:
        Binaries_path = ph.get_path("Binaries.json")
        print("path", Binaries_path)
        json_data = json.loads(Path(Binaries_path).read_text())
    except FileNotFoundError:
        oh.output_handler(is_error=True,message="Binaries.json not found!")

    output = []
    is_txt_file = binary.endswith(".txt")

    if is_txt_file:
        binary_path = Path(binary)

        try:
            content = binary_path.read_text()
        except FileNotFoundError:
            oh.output_handler(is_error=True,message=f"File not found : {binary}")

        match func:
            case "suid":
                binaries = [
                    b.strip().split("/")[-1] for b in content.splitlines() if b.strip()
                ]
            case "capabilities":
                binaries = [
                    b.strip().split(" ")[0] for b in content.splitlines() if b.strip()
                ]
            case _:
                oh.output_handler(
                    with_panel=True,
                    message=f"[bold red]Function '{func}' doesn't support [green]*file.txt*[/green] feature.[/bold red]",
                    title="Unsupported Function",
                    border_style="red",
                )
                return

        if not binaries:
            oh.output_handler(
                with_panel=True,
                message="[bold red]No binaries found in the file.[/bold red]",
                title="Empty File",
            )
            return
    else:
        binaries = [binary]

    # Loop through the JSON data
    for current_binary in binaries:
        for entry in json_data:
            try:
                entries = entry[current_binary][func]
                for item in entries:
                    output.append({"code": item["code"], "binary": current_binary})
            except (KeyError, IndexError):
                continue

    if not output:
        oh.output_handler(
            with_panel=True,
            message=f"[bold yellow]No entries found for function '{func}' and binary '{binary}'.[/bold yellow]",
            title="No Results",
            border_style="yellow",
        )

    for result in output:
        panel = Panel.fit(
            Text.from_markup(
                f"""[bold blue][</>] CODE:
[green]{result['code']}[/green]

[bold blue][+][/bold blue] [bold]Binary:[/bold] [green]{result['binary']}[/green]
[bold blue][+][/bold blue] [bold]Function:[/bold] [green]{func}[/green]"""
            ),
            border_style="cyan",
            title="[bold magenta]GTFO Result[/bold magenta]",
            box=box.ROUNDED,
        )
        console.print(panel)
