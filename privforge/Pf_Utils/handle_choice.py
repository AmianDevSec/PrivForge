import time
from Tools.offline_gtfo import gtfo
from Utils.custom_input import confirm_input, user_input
from Utils.clear import clear
import Utils.output_handler as oh

def handle_choice(choice: str):
    clear()
    
    try:
        match choice:
            case "1":
                oh.output_handler(
                    message="[bold blue][~][/bold blue] Launching Backdoor module...\n"
                )
                time.sleep(1)
                
                from Exploits.backdoor import backdoor_choice
                backdoor_choice()

            case "2":

                import Utils.get_local_ip as get_local_ip
                ip_address = get_local_ip.get_ip()

                attacker_ip = user_input(
                    label="[?] Enter your local machine IP address"
                )

                ssh_port = confirm_input("[?] Is your SSH server port still 22?")
                custom_port = (
                    ""
                    if ssh_port
                    else user_input(label="[?] Enter your custom SSH port")
                )

                oh.output_handler(
                    message="[bold blue][~][/bold blue] Launching NFS Exploitation module...\n"
                )
                time.sleep(1)

                import Exploits.nfs_exploit as nfs_exploit

                nfs_exploit.nfs_exploit(
                    str(ip_address),
                    attacker_ip,
                    # attacker_username,
                    ssh_port="22" if ssh_port else custom_port,
                )

            case "3":
                oh.output_handler(
                    message="[bold blue][~][/bold blue] Launching LD_PRELOAD Exploit...\n"
                )
                time.sleep(1)
                import Exploits.path_exploit as path_exploit

                path_exploit.be_root()

            case "4":
                oh.output_handler(
                    message="[bold blue][~][/bold blue] Launching Offline GTFO module...\n"
                )
                time.sleep(1)

                gtfo()

            case "5":
                oh.output_handler(
                    message="[bold blue][~][/bold blue] Launching Updating ...\n"
                )

                time.sleep(1)
                import Pf_Utils.privforge_updater as pf_up

                pf_up.pf_updater()

            case "6":
                oh.output_handler(
                    message="[bold green][+] Thank you for using  Exiting...[/bold green]\n"
                )
                time.sleep(1)
                exit(0)

            case _:
                oh.output_handler(is_error=True, message="Invalid choice. Try again.")

    except (AssertionError, Exception, KeyboardInterrupt, EOFError) as e:
        pass
