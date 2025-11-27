# utils.py
from datetime import datetime
from config import SORTING_RULES

def get_category(extension):
    """Finds the dictionary key for a given extension."""
    for label, ext_list in SORTING_RULES.items():
        if extension in ext_list:
            return label
    return None

def get_unique_path(target_path):
    """
    If a file exists, appends a timestamp to make the name unique.
    Returns the new unique path.
    """
    if target_path.exists():
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Rename: filename_timestamp.ext
        return target_path.with_name(f"{target_path.stem}_{stamp}{target_path.suffix}")
    return target_path
