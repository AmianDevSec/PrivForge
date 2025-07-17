import Utils.output_handler as oh
from rich.text import Text
from Utils.hero_cli import hero
from Utils.clear import clear
import Pf_Utils.banner as b

def home():
    b.banner()
    menu = Text()
    
    menu.append("┌──[ ", style="bold green")
    menu.append("Privilege Escalation Toolkit", style="bold white")
    menu.append(" ]\n│\n", style="bold green")

    menu.append("│ [1] ", style="bold yellow")
    menu.append("Backdoor\n", style="bold white")
    menu.append("│ [2] ", style="bold yellow")
    menu.append("NFS Exploitation\n", style="bold white")
    menu.append("│ [3] ", style="bold yellow")
    menu.append("LD_PRELOAD Abuse\n", style="bold white")
    menu.append("│ [4] ", style="bold yellow")
    menu.append("Offline GTFO\n", style="bold white")
    menu.append("│ [5] ", style="bold yellow")
    menu.append("Update PrivForge\n", style="bold white")
    menu.append("│ [6] ", style="bold yellow")
    menu.append("Exit\n", style="bold white")

    menu.append("└───────────────\n", style="bold green")
    oh.output_handler(message=menu)
