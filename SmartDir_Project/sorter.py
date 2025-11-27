# sorter.py
import shutil
import os
import time

def move_to_category(item, category_path):
    """Moves file to the category folder"""
    new_path = category_path / item.name
    try:
        shutil.move(item, new_path)
        print(f"{item} moved to -->{new_path}")
        
        # Return new path and mod time for the archiver to use
        modification_time = os.path.getmtime(new_path)
        print(f"The file: {new_path} was last modified at: {time.ctime(modification_time)}")
        return new_path, modification_time
    except OSError as e:
        print(f"Failed to move{item}")
        return None, None
