# SmartDir: Intelligent Modular File Organizer

## 📖 Project Overview
**SmartDir** is a robust Python automation utility designed to eliminate digital clutter. It transforms chaotic folders (like Downloads) into structured workspaces without manual intervention.

This project utilizes a **Modular Architecture**, splitting logic into distinct components (Sorting, Archiving, Configuration) to ensure scalability and maintainability. It employs a dual-layer strategy:
1.  **Semantic Sorting:** Immediately categorizes files into folders (e.g., `IMAGES`, `DOCS`) based on extensions.
2.  **Temporal Archiving:** Identifies files older than a user-defined limit (e.g., 100 days) and offers to either **Archive** or **Delete** them to free up space.

## 🚀 Key Features
* **Modular Codebase:** Logic is distributed across 5 specialized modules (`sorter`, `archiver`, etc.) for better readability and debugging.
* **Dictionary-Based Mapping:** Uses a configurable Hash Map in `config.py` to link 40+ extensions to 7 distinct categories.
* **Interactive Lifecycle Management:** The system calculates file age and asks the user for permission before deleting or archiving old files.
* **Collision Handling:** Automatically renames duplicate files with a timestamp (e.g., `image_20231127.jpg`) to prevent data loss.
* **Cross-Platform:** Built on `pathlib` to work seamlessly on Windows, macOS, and Linux.

## 📂 Project Structure
The solution is engineered into **5 meaningful modules** to satisfy architectural requirements:

| Module | Description |
| :--- | :--- |
| **`main.py`** | **Entry Point.** Orchestrates the user input and calls the sorter/archiver. |
| **`config.py`** | **Settings.** Stores extension rules and folder names. |
| **`sorter.py`** | **Logic.** Handles file categorization and physical movement. |
| **`archiver.py`** | **Logic.** Calculates file age and handles the "Archive vs Delete" decision. |
| **`utils.py`** | **Helpers.** Contains shared functions for timestamping and path validation. |

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Libraries:** `os`, `shutil`, `pathlib`, `datetime`, `time` (Standard Library)

## 💻 Steps to Install & Run

### 1. Prerequisites
Ensure you have Python installed. You can verify this in your terminal:
```bash
python --version

### 2. Installation
cd SmartDir_Project

### 3. Usage:
python main.py
