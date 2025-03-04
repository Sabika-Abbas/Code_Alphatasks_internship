import shutil
import os
from pathlib import Path

source_folder="C:\\sabika"
destination_folder={
    "ppts": ".pptx",
    "document": ".docx",
    "text": ".txt"

}
print("Welcome to File Sorter!")
def move():
    user = input("Move files to:\n1. Existing folder\n2. Automatically sort files into new folders\nEnter choice: ")

    if user == "1":
        for file in os.listdir(source_folder):
            print(file)
        folder_name = input("Enter the name of the existing folder: ")
        folder_path = os.path.join(source_folder, folder_name)

        if os.path.isdir(folder_path):  # Correct folder existence check
            m_file = input("Enter the name of the file to move: ")
            file_path = os.path.join(source_folder, m_file)

            if os.path.isfile(file_path):  # Check if the file exists
                shutil.move(file_path, folder_path)
                print(f"Moved: {m_file} --> {folder_name}")
            else:
                print("File does not exist.")
        else:
            print("Folder does not exist.")

    elif user=="2":
        for file in os.listdir(source_folder):
            file_path = os.path.join(source_folder, file)
            if os.path.isfile(file_path):
                for folder, extension in destination_folder.items():
                    if file.lower().endswith(extension):
                        # Destination folder path
                        dest_path = os.path.join(source_folder, folder)
                        
                        # Create folder if it doesn't exist
                        Path(dest_path).mkdir(parents=True, exist_ok=True)
                        
                        # Move file to respective folder
                        shutil.move(file_path, os.path.join(dest_path, file))
                        print(f"Moved: {file} --> {folder}")


def create_folder():
    new_folder=input("Enter name of folder: ")
    path=f"C:\\sabika\\{new_folder}"
    folder_path = Path(path)
    folder_path.mkdir(parents=True, exist_ok=True)
    print("Folder created successfully!")

def view():
    for file in os.listdir(source_folder):
        print(file)
    x=input("enter name of folder you want to view:")
    file_path = os.path.join(source_folder, x)
    if os.path.isdir(file_path):
        for files in os.listdir(file_path):
            print(files)
    else:
        print("Folder does not exist")


while True:
    print(''' 
            1. Moving files
            2. Creation of folder
            3. View folders
            4. Exit
        ''')
    choice=input("enter your choice: ")

    if choice=="2":
        create_folder()

    elif choice=="1":
        move()

    elif choice=="3":
        view()

    elif choice=="4":
        print("Exiting program...")
        break
    else:
        print("invalid choice")





