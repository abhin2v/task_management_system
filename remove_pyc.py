import os
import shutil

def clean_pyc_and_pycache(start_path="."):
    for root, dirs, files in os.walk(start_path):
        # Remove .pyc files
        for file in files:
            if file.endswith(".pyc"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Removed file: {file_path}")

        # Remove __pycache__ directories
        for dir_name in dirs:
            if dir_name == "__pycache__":
                dir_path = os.path.join(root, dir_name)
                shutil.rmtree(dir_path)
                print(f"Removed directory: {dir_path}")

if __name__ == "__main__":
    clean_pyc_and_pycache(".")  # Change "." to your project root path

