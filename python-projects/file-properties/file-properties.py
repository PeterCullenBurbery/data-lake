import os
import pathlib
import datetime

# File path
file_path = r"C:/GitHub-repositories/data-lake/rust-projects/file_properties/2025_08_24_19_53_46_669.png"

# Use pathlib for easier handling
path_obj = pathlib.Path(file_path)

if path_obj.exists():
    print(f"File Name: {path_obj.name}")
    print(f"Absolute Path: {path_obj.resolve()}")
    print(f"Parent Directory: {path_obj.parent}")
    print(f"File Extension: {path_obj.suffix}")
    print(f"File Stem (name without extension): {path_obj.stem}")
    print(f"File Size: {path_obj.stat().st_size} bytes")

    # File times
    created_time = datetime.datetime.fromtimestamp(path_obj.stat().st_ctime)
    modified_time = datetime.datetime.fromtimestamp(path_obj.stat().st_mtime)
    accessed_time = datetime.datetime.fromtimestamp(path_obj.stat().st_atime)

    print(f"Created Time: {created_time}")
    print(f"Modified Time: {modified_time}")
    print(f"Last Accessed Time: {accessed_time}")
else:
    print(f"The file does not exist: {file_path}")
