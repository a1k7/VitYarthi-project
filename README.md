# SmartDir: Intelligent File Organization System

## 📖 Project Overview
Managing a chaotic "Downloads" folder is a repetitive task that wastes valuable time. **SmartDir** is a modular Python-based automation utility designed to eliminate digital clutter. 

Unlike basic scripts, this project uses a **multi-module architecture** to employ a dual-layer organization strategy:
1. **Semantic Categorization:** Maps files to categories (Images, Code, Music) based on extensions.
2. **Temporal Archiving:** Identifies files unmodified for over **100 days** and migrates them to a dedicated "Archive" sector to keep the active workspace clean.

## 🚀 Key Features
* **Modular Design:** Logic is split across 5 distinct modules (`main`, `sorter`, `archiver`, etc.) for scalability and maintainability.
* **Dictionary-Based Sorting:** Uses a robust Hash Map in `config.py` to link 40+ file extensions to parent categories.
* **Temporal Filter:** Automatically calculates file age and moves dormant files (>100 days) to an archive folder.
* **Safe Execution:** Implements `try-except` blocks in `sorter.py` and `archiver.py` to handle permission errors gracefully.

## 📂 Project Structure
The project is organized into the following modules to ensure separation of concerns:

| File | Purpose |
| :--- | :--- |
| **`main.py`** | The entry point. Orchestrates the workflow by connecting all other modules. |
| **`config.py`** | Stores configuration constants (Extension mappings, Age limits) for easy editing. |
| **`sorter.py`** | Handles the core logic of moving files from the root to category folders. |
| **`archiver.py`** | Contains the time-decay algorithm to identify and move old files. |
| **`utils.py`** | Helper functions for directory creation and extension validation. |

## ⚙️ Logic Flow
1.  **Scan:** `main.py` iterates through the directory using `iterdir()` for memory efficiency.
2.  **Sort:** `sorter.py` moves the file to a category folder (e.g., `/IMAGE`) based on `config.py`.
3.  **Check Age:** Immediately after sorting, `archiver.py` checks if `(Current Time - Mod Time) > 100 Days`.
4.  **Archive:** If old, the file is moved again to `/Archive_files`.

## 💻 Installation & Usage

### 1. Prerequisites
* Python 3.x installed.
* No external libraries required (Uses standard `os`, `shutil`, `pathlib`, `time`).

### 2. Configuration
1.  Open `main.py`.
2.  Update the `download_directory` variable to point to the folder you want to clean:
    ```python
    # In main.py
    download_directory = home_directory / "Your/Target/Path/Here"
    ```
3.  (Optional) Open `config.py` to add new file extensions or change the 100-day limit.

### 3. Execution
Navigate to the project folder in your terminal and run the main script:
```bash
python main.py
