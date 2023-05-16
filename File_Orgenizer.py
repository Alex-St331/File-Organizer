import os
import shutil
from tkinter import filedialog
from tkinter import Tk

def main():
    # Hide the main tkinter window
    root = Tk()
    root.withdraw()

    # Open the folder selection dialog
    folder_path = filedialog.askdirectory()
    if not folder_path:
        print("No folder selected, exiting.")
        return

    # Ensure 'All Files' folder exists
    all_files_folder = os.path.join(folder_path, 'All Files')
    os.makedirs(all_files_folder, exist_ok=True)

    # Create the required folders inside 'All Files'
    folder_dict = {
        'Documents': ['.doc', '.pptx', '.txt', '.pdf'],
        'Videos': ['.mp4', '.avi', '.flv', '.wmv'],
        'Music': ['.mp3', '.wav'],
        'Images': ['.png', '.jpg', '.jpeg', '.gif'],
        'Applications': ['.exe'],
        'Data': ['.csv', '.xlsx'],
        'Archive': ['.zip', '.rar'],
        'Other': []
    }

    for folder, extensions in folder_dict.items():
        os.makedirs(os.path.join(all_files_folder, folder), exist_ok=True)

    # Loop over all files in the directory
    for filename in os.listdir(folder_path):
        # Skip directories
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)

        # Determine the destination folder
        dest_folder = 'Other'
        for folder, extensions in folder_dict.items():
            if ext in extensions:
                dest_folder = folder
                break

        # Move the file
        dest_path = os.path.join(all_files_folder, dest_folder, filename)
        shutil.move(os.path.join(folder_path, filename), dest_path)

if __name__ == "__main__":
    main()
