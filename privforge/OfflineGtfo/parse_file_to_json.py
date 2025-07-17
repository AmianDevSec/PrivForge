from pathlib import Path
import os
import yaml
import json
import platform
import shutil
import Utils.output_handler as oh
import Utils.path_handler as ph

binaries_merged_path = ph.get_path("binaries_merged.txt")
repo_path = ph.get_path("GTFOBins.github.io")
Binaries_path = ph.get_path("Binaries.json")

def fetch_and_merge_files() -> None:
    repo_name = repo_path.split('/')[-1]
    url = f"https://github.com/GTFOBins/{repo_name}.git"

    # Remove existing clone if it exists
    if Path(repo_path).exists():
        oh.output_handler(message="[yellow]Removing existing GTFOBins repo...[/yellow]")
        shutil.rmtree(repo_path)

    oh.output_handler(message=f"[cyan]Cloning [bold]{url}[/bold][/cyan]")

    os.system(f"git clone {url}")

    # Locate _gtfobins folder inside the repo
    gtfobins_path = Path(repo_path) / "_gtfobins"

    oh.output_handler(is_error=gtfobins_path.exists(), message="Error: _gtfobins folder not found.")

    merged_file = Path(binaries_merged_path)

    with merged_file.open("w", encoding="utf-8") as outfile:
        for md_file in sorted(gtfobins_path.glob("*.md")):
            
            # Inject filename for later mapping
            outfile.write(f"#FILENAME: {md_file.stem}\n")
            outfile.write(md_file.read_text(encoding="utf-8"))
            outfile.write("\n+")

    return oh.output_handler(
        message=f"[green]Merged markdown files into [bold]{merged_file}[/bold][/green]"
    )


def handle_binaries_file():
    md_path = Path(binaries_merged_path)
    oh.output_handler(is_error=md_path.exists(),message="Error: Merged file not found!")

    md_content = md_path.read_text()
    blocks = [block.strip() for block in md_content.split("+") if block.strip()]

    blocks_v2 = [block.removesuffix('---') for block in blocks]

    parsed_blocks = []

    for block in blocks_v2:
        lines = block.split("---")

        filename = lines[0].replace("#FILENAME: ", "").strip()
        yaml_content = "\n".join(lines[1:])

        try:
            parsed = yaml.safe_load(yaml_content)

            if parsed and "functions" in parsed:
                parsed_blocks.append({filename: parsed["functions"]})

        except yaml.YAMLError as e:
            return oh.output_handler(
                with_panel=True,
                message=f"YAML parsing error in [bold]{filename}[/bold]:\n{e}",
                border_style="red",
            )

    oh.output_handler(
        is_error=not bool(parsed_blocks), 
        message="No YAML blocks were parsed. Check the format of markdown files."
    )

    with open(Binaries_path, "w", encoding="utf-8") as f:
        json.dump(parsed_blocks, f, indent=2, ensure_ascii=False)

    # Cleanup
    if Path(binaries_merged_path).exists():
        Path(binaries_merged_path).unlink()

    if Path(repo_path).exists():
        shutil.rmtree(repo_path)

    return oh.output_handler(message="[bold green]✔ Successfully updated Binaries.json[/bold green]")


def update_handler() -> None:
    oh.output_handler(
        is_error=platform.system() != "Linux",
        message="Platform unsupported. This script runs on Linux only.",
    )

    fetch_and_merge_files()
    handle_binaries_file()


if __name__ == "__main__":
    update_handler()
