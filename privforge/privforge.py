from privforge.utils import (
    output_handler as oh,
    home as h,
    handle_choice as hc,
    output_handler as oh,
    custom_input as ci
)

def start_privforge():
    
    while True:
        h.home()
        
        try:
            choice = ci.user_input(
                choices=["1", "2", "3", "4", "5", "6"], label="[?] Select an option", default="1"
            )
            
            hc.handle_choice(choice.strip())
            input("\n[Press ENTER to return to menu...]")

        except (AssertionError, Exception, KeyboardInterrupt, EOFError):

            oh.output_handler(is_error=True,message="Interrupted by user. Exiting...")
            break

def main():
    start_privforge()
    
if __name__ == "__main__":
    main()