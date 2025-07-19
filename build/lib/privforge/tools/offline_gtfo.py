from privforge.utils import (
    output_handler as oh,
    custom_input as ci
)

from privforge.offline_gtfo_utils import (
    menu as m, 
    handle_choice as hc
)

def gtfo():
    while True:
        m.menu()
        try:
            choice = ci.user_input(
                choices=["1", "2", "3"], label="[?] Select an option", default="1"
            )
            result = hc.handle_choice(choice.strip())
            if result == "exit":
                break 

            input("\n[Press ENTER to return to menu...]")

        except KeyboardInterrupt:
            oh.output_handler(is_error=True, message="Interrupted. Returning to main menu...")
            break

if __name__ == "__main__":
    gtfo()