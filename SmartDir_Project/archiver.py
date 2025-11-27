# archiver.py
import time
import shutil
from config import LIMIT_SECONDS

def check_and_archive(new_path, modification_time, base_directory):
    """Checks age and moves to archive if old"""
    current_time = time.time()
    age_of_file = current_time - modification_time
    
    if age_of_file > LIMIT_SECONDS:
        archive_directory = base_directory / "Archive_files"
        archive_directory.mkdir(exist_ok=True)
        
        final_destination = archive_directory / new_path.name
        
        # Move 2: Archive it
        try:
            shutil.move(new_path, final_destination)
            print(f" File is old ({int((age_of_file)/86400)} days). Moved to Archive folder.")
            
            # Your original input logic
            Question = input("Do you want to delete the archived files: ")
            answer = Question.lower()
            if answer == 'yes':
                # Note: Your original code asked but didn't actually delete in the snippet provided.
                # I have kept it exactly as you wrote it (just asking).
                pass
        except OSError:
            print(f"Failed to archive {new_path.name}")
    else:
        # Just getting category name from path for print statement
        print(f"File is recently added. Keeping in folder.")
