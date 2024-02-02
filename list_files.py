# import os
#
# folders = input("Enter the list of folder names in space between: ").split()
# for folder in folders:
#     try:
#         files = os.listdir(folder)
#         print(f"#########listing files for the folder - {folder}")
#     except FileNotFoundError:
#         print(f"Please Enter a valid folder name. The {folder} does not exist")
#         continue
#     except PermissionError:
#         print(f"No Access to this folder {folder}")
#
#     for file in files:
#         print(file)

import os


def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files , None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission Denied"


def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    for folder in folder_paths:
        files, error_message = list_files_in_folder(folder)
        if files:
            print(f"The files in folder path {folder} are ======")
            for name in files:
                print(name)
        else:
            print(f"Error in {folder}. The error message: {error_message}")


if __name__ == "__main__":
    main()
