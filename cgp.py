from pathlib import Path
import os
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Directory for storing files
BASE_DIR = Path("files")
BASE_DIR.mkdir(exist_ok=True)


# ---------------------------------------------
# Utility: List all files with details
# ---------------------------------------------
def list_files():
    print(Fore.YELLOW + "\n========== AVAILABLE FILES ==========\n")

    files = list(BASE_DIR.glob("*"))

    if not files:
        print(Fore.RED + "No files available.\n")
        return []

    for idx, file in enumerate(files, start=1):
        size = os.path.getsize(file)
        modified = datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y-%m-%d %H:%M:%S")

        print(f"{idx}. {file.name}  | Size: {size} bytes | Modified: {modified}")

    print()
    return files


# ---------------------------------------------
# CREATE FILE
# ---------------------------------------------
def create_file():
    try:
        list_files()
        file_name = input("Enter new file name: ").strip()

        if not file_name:
            print(Fore.RED + "File name cannot be empty.\n")
            return

        file_path = BASE_DIR / file_name

        if file_path.exists():
            print(Fore.RED + "File already exists!\n")
            return

        content = input("Enter content (leave blank for empty file): ")

        with open(file_path, "w") as f:
            f.write(content)

        print(Fore.GREEN + "File created successfully!\n")

    except Exception as err:
        print(Fore.RED + f"Error: {err}\n")


# ---------------------------------------------
# READ FILE
# ---------------------------------------------
def read_file():
    try:
        files = list_files()
        if not files:
            return

        file_name = input("Enter file name to read: ").strip()
        file_path = BASE_DIR / file_name

        if not file_path.exists():
            print(Fore.RED + "File does not exist.\n")
            return

        print(Fore.CYAN + "\n====== FILE CONTENT ======\n")

        with open(file_path, "r") as f:
            print(f.read())

        print(Fore.CYAN + "\n==========================\n")

    except Exception as err:
        print(Fore.RED + f"Error: {err}\n")


# ---------------------------------------------
# UPDATE FILE
# ---------------------------------------------
def update_file():
    try:
        files = list_files()
        if not files:
            return

        file_name = input("Enter file name to update: ").strip()
        file_path = BASE_DIR / file_name

        if not file_path.exists():
            print(Fore.RED + "File does not exist.\n")
            return

        print(Fore.YELLOW + """
====== UPDATE OPTIONS =======
1. Rename File
2. Append Content
3. Overwrite Content
=============================
        """)

        choice = input("Choose option (1/2/3): ").strip()

        # ----- Rename -----
        if choice == "1":
            new_name = input("Enter new file name: ").strip()
            new_path = BASE_DIR / new_name

            if new_path.exists():
                print(Fore.RED + "File with that name already exists.\n")
                return

            file_path.rename(new_path)
            print(Fore.GREEN + "File renamed successfully!\n")

        # ----- Append -----
        elif choice == "2":
            extra = input("Enter content to append: ")
            with open(file_path, "a") as f:
                f.write("\n" + extra)
            print(Fore.GREEN + "Content appended!\n")

        # ----- Overwrite -----
        elif choice == "3":
            new_data = input("Enter new content: ")
            with open(file_path, "w") as f:
                f.write(new_data)
            print(Fore.GREEN + "File overwritten successfully!\n")

        else:
            print(Fore.RED + "Invalid option.\n")

    except Exception as err:
        print(Fore.RED + f"Error: {err}\n")


# ---------------------------------------------
# DELETE FILE
# ---------------------------------------------
def delete_file():
    try:
        files = list_files()
        if not files:
            return

        file_name = input("Enter file name to delete: ").strip()
        file_path = BASE_DIR / file_name

        if not file_path.exists():
            print(Fore.RED + "File does not exist.\n")
            return

        confirm = input(Fore.RED + "Are you sure? (yes/no): ").lower()[0]

        if confirm == "yes":
            file_path.unlink()
            print(Fore.GREEN + "File deleted successfully!\n")
        else:
            print(Fore.YELLOW + "Delete operation cancelled.\n")

    except Exception as err:
        print(Fore.RED + f"Error: {err}\n")


# ---------------------------------------------
# MAIN MENU
# ---------------------------------------------
def main():
    while True:
        print(Fore.BLUE + """
===================================
       FILE HANDLING SYSTEM
===================================
1. Create File
2. Read File
3. Update File
4. Delete File
5. Exit
===================================
        """)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            update_file()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            print(Fore.MAGENTA + "Goodbye! Exiting program...\n")
            break
        else:
            print(Fore.RED + "Invalid choice! Try again.\n")


# Run program
if __name__ == "__main__":
    main()
