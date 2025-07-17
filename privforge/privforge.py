from Utils.custom_input import user_input
import Utils.output_handler as oh
from Pf_Utils.home import home
from Pf_Utils.handle_choice import handle_choice

def start_privforge():
    
    while True:
        home()
        
        try:
            choice = user_input(
                choices=["1", "2", "3", "4", "5", "6"], label="[?] Select an option", default="1"
            )
            
            handle_choice(choice.strip())
            input("\n[Press ENTER to return to menu...]")

        except (AssertionError, Exception, KeyboardInterrupt, EOFError):

            oh.output_handler(is_error=True,message="Interrupted by user. Exiting...")
            break

if __name__ == "__main__":
    start_privforge()