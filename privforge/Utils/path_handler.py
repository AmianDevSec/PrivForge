import os
import importlib.resources as resources
import tempfile
import shutil

def get_path(file: str) -> str:
    """
    Returns the filesystem path to a resource file.

    If the resource exists on the filesystem (e.g. during development),
    returns the direct path.

    Otherwise, extracts the resource to a temporary file and returns that path.

    Args:
        file (str): Relative path inside the package, e.g. 'data/Binaries.json'

    Returns:
        str: Absolute filesystem path to the resource file
    """
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, file)

    if os.path.exists(full_path):
        # Local dev path available
        return full_path
    else:
        # Extract resource to a temp file
        package = __package__ or 'privforge'
        
        # Split folder and filename
        parts = file.replace(os.sep, '/').split('/')
        *pkg_parts, filename = parts
        pkg = f"{package}." + ".".join(pkg_parts) if pkg_parts else package

        # Read resource as binary and write to temp file
        with resources.open_binary(pkg, filename) as resource_stream:
            tmp_file = tempfile.NamedTemporaryFile(delete=False)
            shutil.copyfileobj(resource_stream, tmp_file)
            tmp_file.close()
            return tmp_file.name
