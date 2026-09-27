"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Salvaaodr, Adrian G.]
Date: [9/27/2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
A code that will read each file pdf, jpg, mp3 etc. after the code run it will make a folder 
for each file. The script checks the files inside a folder and identifies whether each
file is an image, document, or music file. It then moves the
file to the appropriate folder. 


============================================
KEY VOCABULARY
============================================
- os module: A Python module that allows a program to interact
  with files, folders, and parts of the operating system.
- shutil module:  A Python module used for operations involving
  files and folders, such as moving or copying files.
- file path: The location that tells the computer where a file
  or folder is stored.
- directory: Another name for a folder that contains files or
  other folders.
- file extension: The part at the end of a filename that
  identifies the file type, such as .jpg or .pdf.
- os.listdir(): A function that gets the names of files and
  folders inside a directory.
- shutil.move(): A function that moves a file from one location
  to another.


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# Folder containing the files to organize
source_folder = "module-2-python-basics/file-sorting-test"

# Folders for different file types
images_folder = os.path.join(source_folder, "Images")
documents_folder = os.path.join(source_folder, "Documents")
music_folder = os.path.join(source_folder, "Music")

# Create the folders if they do not already exist
os.makedirs(images_folder, exist_ok=True)
os.makedirs(documents_folder, exist_ok=True)
os.makedirs(music_folder, exist_ok=True)

# Check every file in the source folder
for file_name in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file_name)

    # Skip folders
    if os.path.isfile(file_path):

        # Get the file extension
        extension = os.path.splitext(file_name)[1].lower()

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            shutil.move(file_path, images_folder)

        elif extension in [".pdf", ".txt", ".docx"]:
            shutil.move(file_path, documents_folder)

        elif extension in [".mp3", ".wav"]:
            shutil.move(file_path, music_folder)

print("Files have been sorted!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I made was using the wrong path for the file-sorting-test folder. 
I initially used "file-sorting-test" as the source folder, but my test folder was 
actually inside the module-2-python-basics folder. Because of this, the program created another 
file-sorting-test folder in the wrong location instead of using the folder where my files were stored.
I fixed it by changing the path to "module-2-python-basics/file-sorting-test". 
This taught me that the file path needs to match the actual location of the folder so Python can 
find and organize the files correctly.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
