from OfflineGtfo.functions_handler import functions, show_functions
from Utils.clear import clear
import time
import Utils.output_handler as oh
from OfflineGtfo.parse_file_to_json import update_handler
from OfflineGtfo.search_binary import search_binary
from Utils.custom_input import user_input

def handle_choice(choice: str):
    clear()
    
    match choice:
        case "1":
            oh.output_handler(
                message="[bold blue][~][/bold blue] Search binary functionality...\n"
            )
            binary = user_input(
                label="[?] Enter binary's name (or path to file with binaries)"
            )
            func = user_input(label="[?] Enter function to search").lower()

            if func not in functions:
                oh.output_handler(
                    message=f"[bold red]Unsupported function: {func}[/bold red]\nUse option [bold yellow]2[/bold yellow] to view available functions.",
                    title="Error",
                    border_style="red",
                    with_panel=True,
                )
                return
            
            search_binary(binary, func)

        case "2":
            show_functions()

        case "3":
            oh.output_handler(
                message="[bold yellow][~][/bold yellow] Updating database...\n"
            )
            update_handler()
            oh.output_handler(message="[bold green]✔ Update complete!")

        case "4":
            oh.output_handler(
                message="[bold green][+] Returning to main menu...[/bold green]"
            )
            
            time.sleep(1)
            return "exit"

        case _:
            oh.output_handler(is_error=True, message="Invalid choice. Try again.")
