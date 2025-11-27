# config.py

# Your original mapping logic
File_extension = {
    ".jpeg": "IMAGE", ".jpg": "IMAGE", ".png": "IMAGE", ".gif": "IMAGE",
    ".svg": "IMAGE", ".tif": "IMAGE", ".tiff": "IMAGE", ".cr2": "IMAGE",
    ".nef": "IMAGE", ".arw": "IMAGE", ".heif": "IMAGE", ".avif": "IMAGE",
    ".pdf": "DOCUMENT", ".doc": "DOCUMENT", ".docx": "DOCUMENT",
    ".txt": "DOCUMENT", ".rtf": "DOCUMENT", ".odt": "DOCUMENT",
    ".xls": "DOCUMENT", ".xlsx": "DOCUMENT", ".csv": "DOCUMENT",
    ".ppt": "DOCUMENT", ".pptx": "DOCUMENT",
    ".htm": "HTML-DOCUMENT", ".html": "HTML-DOCUMENT", ".php.html": "HTML-DOCUMENT",
    ".apk": "APPLICATIONS",
    ".wav": "SONGS", ".aiff": "SONGS", ".pcm": "SONGS", ".flac": "SONGS",
    ".alac": "SONGS", ".mp3": "SONGS", ".mp4": "SONGS", ".aac": "SONGS",
    ".m4a": "SONGS", ".wma": "SONGS",
    ".py": "PYTHON_SCRIPTS", ".js": "JAVASCRIPT", ".jsx": "JAVASCRIPT",
    ".cjs": "JAVASCRIPT", ".mjs": "JAVASCRIPT", ".tsx": "JAVASCRIPT",
    ".cpp": "C/C++",
    ".ics": "CALENDER", 
    ".pkg": "PACKAGES",
}

# Your time limit logic
DAYS_TO_KEEP = int(input("Enter after how many days you want move your files to Archive."))
LIMIT_SECONDS = DAYS_TO_KEEP * 86400
