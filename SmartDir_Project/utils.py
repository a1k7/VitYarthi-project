# utils.py
import os
from pathlib import Path
from config import File_extension

def get_category(item):
    """Checks if file extension exists in our dictionary"""
    ext = item.suffix.lower()
    if ext in File_extension:
        return File_extension[ext]
    return None

def create_folder(parent_path, folder_name):
    """Creates directory if absent"""
    category_path = parent_path / folder_name
    category_path.mkdir(exist_ok=True)
    return category_path
