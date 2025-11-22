# SmartDir: Intelligent File Organization System

## 📖 Project Overview
Managing a chaotic "Downloads" or any workspace folder is a repetitive task that wastes valuable time. **SmartDir** is a Python-based automation utility designed to eliminate digital clutter. Unlike basic sorters, this script employs a dual-layer organization strategy: first, it maps files to specific semantic categories (like Images, Code, or Music) based on their extensions. Second, it applies a **temporal filter**, identifying files that have been dormant (unmodified) for over that many days user wants to keep it and migrating them to a dedicated "Archive" sector if it exceeds the days limit specified by the user. This ensures your active workspace remains relevant and clean.

## 🚀 Key Features
* **Dictionary-Based Sorting:** Utilizes a robust Hash Map (Dictionary) to link over 40+ file extensions (e.g., `.py`, `.docx`, `.flac`) to their respective parent categories.
* **Temporal Archiving Logic:** Implements a time-decay algorithm that calculates the delta between `CURRENT TIME` and the file's `MODIFICATION TIME`. Files exceeding the **8.64 million second** threshold (100 days) are automatically archived.
* **Interactive Clean-up:** The script doesn't just move files; it communicates with the user via the console, asking for permission to purge empty archive folders after operations are complete.
* **Safe-Fail Execution:** Uses `try-except` blocks around `shutil` operations to prevent the script from crashing due to permission errors or open files.

## ⚙️ Algorithms & Loop Implementation
The core engine of this project relies on `pathlib` for efficient filesystem traversal. The logic follows this specific flow:

1.  **The `iterdir()` Traversal:**
    Instead of loading all file paths into memory at once, the script uses a generator loop:
    ```python
    for entry in root_directory.iterdir():
    ```
    This iterates through the directory entries one by one, ensuring low memory usage even in folders with thousands of files.

2.  **Condition-Based Pipeline:** Inside the loop, every item passes through a filter:
    * **Is it a file?** (`entry.is_file()`) -> specific extensions are extracted.
    * **Map & Move:** The extension acts as a key to look up the destination folder. If the folder is missing, `mkdir(exist_ok=True)` handles it dynamically.
    * **Age Assessment:** The loop immediately checks the file's age after moving it. If `(Current_Time - Last_Modified) > 100 Days`, a secondary move triggers, shifting the file to the Archive.

## 🛠️ Tech Stack
| Component | Technology Used | Purpose |
| :--- | :--- | :--- |
| **Core Logic** | **Python 3.x** | The backbone of the automation script. |
| **Filesystem** | **pathlib** & **os** | Object-oriented path handling and OS-level interactions. |
| **Operations** | **shutil** | High-level file operations (Moving, removing directories). |
| **Timing** | **time** module and datetime module | Epoch timestamp calculations for the 100-day logic. |

## 💻 Steps to Install & Run

### 1. Environment Setup
Ensure you have a Python 3 interpreter installed. No external `pip` packages are required as the script uses standard libraries.

### 2. Configuration
Clone the repo and open the script. You **must** customize the target path variable to match your local machine's user structure:

python
# LOCATE THIS LINE IN THE CODE:
root_directory = Path.home() / "path"(Here, path is user specified as user can give the path of his/her folder which he/she wants to sort.)
archive_spot = root_directory / "Old_Stored_Items"

### 3. Execution
Save code as a plain text on your device.
Navigate to the directory via your terminal and trigger the script:
python your_filename.py

### 4. 🧪 Instructions for Testing
a)Mock Data Creation: Create a temporary folder and place a mix of files inside (e.g., a .jpg image, a .pdf document, and a .mp3 file).
b)Simulate Age (Optional): To test the archiving feature, you can temporarily modify the script's days_to_keep variable to 0. This forces the script to treat all files as "old."
c)Run the Script: Execute the command python sort_files.py.
d)Verify Categorization: Check if the folders IMAGE, DOCUMENT, and SONGS were created and if files were moved correctly.
e)Verify Archiving: Ensure files met the age criteria were moved to the Archive_files folder.
f)Test Interaction: When the console asks "Do you want to delete the archived files?", type no to verify the files are preserved.


Created by: Akhilesh Warik
Registration no. 25BAI10078
