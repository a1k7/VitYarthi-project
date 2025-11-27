# archiver.py
import os
import time
import shutil
from datetime import datetime
import utils
from config import ARCHIVE_FOLDER_NAME

def process_age_check(file_path, root_directory, keep_limit):
    """
    Checks if file is older than limit. 
    Asks user to Delete (Yes) or Archive (No).
    """
    if not file_path.exists():
        return

    try:
        # Check Age
        modified_time = file_path.stat().st_mtime
        file_age_days = (time.time() - modified_time) / 86400

        if file_age_days > keep_limit:
            
            # Prepare Archive Path
            archive_spot = root_directory / ARCHIVE_FOLDER_NAME
            if not archive_spot.exists():
                archive_spot.mkdir(parents=True, exist_ok=True)

            print(f"   -> File is {int(file_age_days)} days old.")
            question = input(f"   -> Do you want to DELETE '{file_path.name}'? (yes/no): ")

            if question.lower() == "yes":
                os.remove(file_path)
                print(f"      [DELETED] (Age: {int(file_age_days)} days)")
            
            elif question.lower() == "no":
                # Move to Archive
                archive_target = archive_spot / file_path.name
                # Handle duplicates in archive
                archive_target = utils.get_unique_path(archive_target)
                
                shutil.move(file_path, archive_target)
                print(f"      [ARCHIVED] Moved to {ARCHIVE_FOLDER_NAME}")
                
        else:
            print(f"   -> File is fresh ({int(file_age_days)} days). Keeping it.")

    except Exception as e:
        print(f"[ERROR] Archiving {file_path.name}: {e}")
