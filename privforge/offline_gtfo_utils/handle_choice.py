import time

from privforge.utils import (
    custom_input as ci,
    output_handler as oh,
    clear as cl
)

from privforge.offline_gtfo_utils import (
    search_binary as sb,
    functions_handler as fh
)

def handle_choice(choice: str):
    cl.clear()
    
    match choice:
        case "1":
            oh.output_handler(
                message="[bold blue][~][/bold blue] Search binary functionality...\n"
            )
            binary = ci.user_input(
                label="[?] Enter binary's name (or path to file with binaries)"
            )
            func = ci.user_input(label="[?] Enter function to search").lower()

            if func not in fh.functions:
                oh.output_handler(
                    message=f"[bold red]Unsupported function: {func}[/bold red]\nUse option [bold yellow]2[/bold yellow] to view available functions.",
                    title="Error",
                    border_style="red",
                    with_panel=True,
                )
                return
            
            sb.search_binary(binary, func)

        case "2":
            fh.show_functions()
            
        case "3":
            oh.output_handler(
                message="[bold green][+] Returning to main menu...[/bold green]"
            )
            
            time.sleep(1)
            return "exit"

        case _:
            oh.output_handler(is_error=True, message="Invalid choice. Try again.")
