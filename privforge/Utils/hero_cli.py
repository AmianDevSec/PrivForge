import pyfiglet
from rich.text import Text
import Utils.output_handler as oh

def hero() -> None: 
    
    # Generate ASCII banner
    ascii_banner = pyfiglet.figlet_format("PrivForge", font="slant")

    # Author/contact info
    info = """
    [bold cyan]Author:[/]      [white]Amian DevSec[/]
    [bold cyan]Mail:[/]        [white]amiandevsec@gmail.com[/]
    [bold cyan]GitHub:[/]      [white]https://github.com/AmianDevSec[/]
    [bold cyan]Coffee:[/]      [white]https://ko-fi.com/amiandevsec[/]
    [bold cyan]LinkedIn:[/]    [white]https://linkedin.com/in/amian-devsec[/]
    """

    # Combine banner and info
    full_text = f"{ascii_banner}\n{info}"
    styled_text = Text.from_markup(full_text)

    # Display the final styled panel
    oh.output_handler(message=styled_text, with_panel=True, border_style="bold green")
