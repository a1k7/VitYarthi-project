# main.py
import os
from pathlib import Path
import sorter
import archiver

def main():
    print("=========================================")
    print("      SMARTDIR - MODULAR EDITION         ")
    print("=========================================")

    # 1. User Input
    path_input = input("Enter the path of your folder you want to sort: ")
    
    # Path Handling
    root_directory = Path.home() / path_input
    
    if not root_directory.exists():
        print(f"Error: The path '{root_directory}' does not exist.")
        return

    try:
        keep_limit = int(input("Enter days limit before archiving/deleting: "))
    except ValueError:
        print("Invalid number. Defaulting to 100 days.")
        keep_limit = 100

    print("\n--------- PROCESS STARTED ---------\n")

    # 2. Main Loop
    # We use list() to avoid issues if files are moved while iterating
    all_files = [f for f in root_directory.iterdir() if f.is_file()]

    for entry in all_files:
        
        # Step A: Sort the file
        new_path = sorter.process_file_sort(entry, root_directory)
        
        # Step B: Check age (only if sorting was successful)
        if new_path:
            archiver.process_age_check(new_path, root_directory, keep_limit)

    print("\n--------- PROCESS COMPLETE ---------\n")
    print("Current working directory:", os.getcwd())

if __name__ == "__main__":
    main()
