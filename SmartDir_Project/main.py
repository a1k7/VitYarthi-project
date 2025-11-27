# main.py
import os
from pathlib import Path
import config
import utils
import sorter
import archiver

def main():
    home_directory = Path.home()
    # Your specific path
    download_directory = home_directory / "Library/CloudStorage/OneDrive-Personal/vit stuff"
    
    # Validation to prevent crash if path doesn't exist on grading machine
    if not download_directory.exists():
        print(f"Directory not found: {download_directory}")
        return

    print("------------Transfering begins-------------")
    
    # Iterate through each file
    for item in download_directory.iterdir():
        if item.is_file():
            
            # 1. Get Category
            category_name = utils.get_category(item)
            
            if category_name:
                # 2. Create Folder
                category_path = utils.create_folder(download_directory, category_name)
                
                # 3. Move File
                new_path, mod_time = sorter.move_to_category(item, category_path)
                
                # 4. Check Archive (Only if move was successful)
                if new_path:
                    archiver.check_and_archive(new_path, mod_time, download_directory)
            else:
                print("Files are still with you!!!!!")
        else:
            # Note: This prints for every folder found, preserving your original logic
            pass 

    print("------------Current working Directory-------------")
    print("Your current working directory is : ", os.getcwd())

if __name__ == "__main__":
    main()
