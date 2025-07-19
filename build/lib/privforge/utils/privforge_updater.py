import subprocess as sub
import sys
import privforge.utils.output_handler as oh

def pf_updater() -> None:
    try:
        oh.output_handler(message="[bold yellow]Updating PrivForge via pip...")

        sub.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "privforge"],
            check=True
        )

        oh.output_handler(message="[bold green]✔ Update complete!")

    except sub.CalledProcessError as e:
        oh.output_handler(
            is_error=True,
            message="Update failed. Try manually with: pip install --upgrade privforge",
            error_detail=e.stderr.decode() if e.stderr else None
        )
    except Exception as e:
        oh.output_handler(
            is_error=True,
            message=f"An error occurred during update: {e}"
        )
