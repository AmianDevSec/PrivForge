from Utils.custom_input import  user_input
import Utils.output_handler as oh
from OfflineGtfo.menu import menu
from OfflineGtfo.handle_choice import handle_choice

def gtfo():
    
    while True:
        menu()
        try:
            choice = user_input(
                choices=["1", "2", "3", "4"], label="[?] Select an option", default="1"
            )
            result = handle_choice(choice.strip())
            if result == "exit":
                break 

            input("\n[Press ENTER to return to menu...]")

        except KeyboardInterrupt:
            oh.output_handler(is_error=True, message="Interrupted. Returning to main menu...")
            break

if __name__ == "__main__":
    gtfo()