import os
from typing import Optional

def get_files_info(working_directory: str, directory: Optional[str]=None):
    try:
        if directory is None:
            directory = "."
        full_path = os.path.abspath(os.path.join(working_directory, directory))
        # Build absolute paths
        abs_working_dir = os.path.abspath(working_directory)

        # Ensure full_path is inside working_directory
        if not (full_path == abs_working_dir or full_path.startswith(abs_working_dir + os.sep)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if full_path is a directory
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        # List directory contents
        entries = []
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            is_dir = os.path.isdir(entry_path)
            try:
                size = os.path.getsize(entry_path)
            except Exception:
                size = 0
            entries.append(f' - {entry}: file_size={size} bytes, is_dir={is_dir}')
        return "\n".join(entries)
    except Exception as e:
        return f"Error: {str(e)}"


print(get_files_info("calculator", None))