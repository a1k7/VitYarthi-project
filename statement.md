# Project Statement: SmartDir

## 1. Problem Statement
For most computer users, the "Downloads" folder is a mess. We download images, PDFs, songs, and setup files every day, and they all pile up in one place. Finding a specific file becomes difficult, and the folder looks cluttered. Sorting these files one by one is boring and takes a lot of time. Because of this, many users just leave their folders disorganized. We need a simple tool that can automatically clean up this mess and keep our computer organized without us having to do it manually.

## 2. Scope of the Project
This project is a desktop automation tool designed to organize files on your local computer.
* **What it does:**
    * It looks through a specific folder (like Downloads or OneDrive).
    * It identifies what kind of file each item is (Image, Document, Song, etc.).
    * It creates new folders for these categories and moves the files into them.
    * It checks if a file hasn't been touched in 100 days and moves it to a separate "Archive" folder to keep the main area clean.
* **What it does not do:**
    * It does not organize emails or cloud files (like Google Drive online).
    * It does not open or read the content of your files; it only looks at the file name and date.

## 3. Target Users
* **Students:** Who have hundreds of study notes, PDFs, and assignment files mixed up.
* **Developers:** Who have code files (`.py`, `.cpp`) mixed with other random downloads.
* **General Users:** Anyone who wants a clean desktop but doesn't have the time to organize it every day.
* **Designers:** Who need to separate their image files (`.png`, `.jpg`) from other documents quickly.

## 4. High-Level Features
* **Automatic Sorting:** Instantly moves files into the correct folder based on their type (e.g., all `.jpg` files go to the "IMAGE" folder).
* **Old File Archiver:** Automatically finds files that are older than 100 days and moves them to an "Archive" folder so they don't clutter your current work.
* **Smart Folder Creation:** If a folder (like "SONGS") doesn't exist yet, the program creates it for you automatically.
* **Safe Cleanup:** The program talks to you; it tells you what it moved and asks for your permission before deleting any empty archive folders.
