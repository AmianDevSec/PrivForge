import time
from privforge.tools.offline_gtfo import gtfo

from privforge.utils import (
    output_handler as oh,
    clear as cl,
    custom_input as ci,
    get_local_ip as lp,
    privforge_updater as pf_up
)

from privforge.exploits import (
    nfs_exploit as nfs,
    backdoor as bk,
    path_exploit as phe
)

def handle_choice(choice: str):
    cl.clear()
    
    try:
        match choice:
            case "1":
                oh.output_handler(
                    message="[bold blue][~][/bold blue] Launching Backdoor module...\n"
                )
                time.sleep(1)
                
                bk.backdoor_choice()

            case "2":

                ip_address = lp.get_ip()

                attacker_ip = ci.user_input(
                    label="[?] Enter your local machine IP address"
                )

                ssh_port = ci.confirm_input("[?] Is your SSH server port still 22?")
                custom_port = (
                    ""
                    if ssh_port
                    else ci.user_input(label="[?] Enter your custom SSH port")
                )

                oh.output_handler(
                    message="[bold blue][~][/bold blue] Launching NFS Exploitation module...\n"
                )
                time.sleep(1)

                nfs.nfs_exploit(
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

                phe.be_root()

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
