# sorter.py
import shutil
import utils

def process_file_sort(entry, root_directory):
    """
    Moves a file to its category folder. 
    Returns the new path if successful, or None if skipped/failed.
    """
    extension = entry.suffix.lower()
    category_found = utils.get_category(extension)

    # Skip uncategorized
    if category_found is None:
        print(f"[UNSORTED] {entry.name} — ignored")
        return None

    # Create category folder
    target_folder = root_directory / category_found
    if not target_folder.exists():
        target_folder.mkdir(parents=True, exist_ok=True)

    # Handle duplicates
    raw_location = target_folder / entry.name
    new_location = utils.get_unique_path(raw_location)

    try:
        shutil.move(entry, new_location)
        print(f"[PLACED] {entry.name}  -> {category_found}")
        return new_location
    except Exception as e:
        print(f"[ERROR] Moving {entry.name}: {e}")
        return None
