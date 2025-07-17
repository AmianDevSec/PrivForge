from Utils.clear import clear
from rich.text import Text
import Utils.output_handler as oh

def menu():
    clear()
    menu = Text()

    menu.append("┌──[ ", style="bold green")
    menu.append("Offline GTFO Menu", style="bold white")

    menu.append(" ]\n│\n", style="bold green")
    menu.append("│ [1] ", style="bold yellow")
    menu.append("Search Binary Capability\n", style="bold white")
    
    menu.append("│ [2] ", style="bold yellow")
    menu.append("List Available Functions\n", style="bold white")
    
    menu.append("│ [3] ", style="bold yellow")
    menu.append("Update Binary Database\n", style="bold white")
    
    menu.append("│ [4] ", style="bold yellow")
    menu.append("Exit\n", style="bold white")
    
    menu.append("└───────────────\n", style="bold green")

    oh.output_handler(message=menu)
