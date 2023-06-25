import os
import shutil
from pathlib import Path

def organize_files(source_directory, destination_directory):
    source_directory = Path(source_directory)
    destination_directory = Path(destination_directory)

    for i in range(1, 6):
        folder_path = destination_directory / f"summary{i}/{source_directory}"
        folder_path.mkdir(parents=True, exist_ok=True)

    folder_path = destination_directory / f"text/{source_directory}"
    folder_path.mkdir(parents=True, exist_ok=True)

    extension_map = {
        ".A": destination_directory / f"summary1/{source_directory}",
        ".B": destination_directory / f"summary2/{source_directory}",
        ".C": destination_directory / f"summary3/{source_directory}",
        ".D": destination_directory / f"summary4/{source_directory}",
        ".E": destination_directory / f"summary5/{source_directory}",
        ".txt": destination_directory / f"text/{source_directory}"
    }

    for root, dirs, files in os.walk(source_directory):
        for file in files:
            file_extension = os.path.splitext(file)[1]

            if file_extension in extension_map:
                destination_folder = extension_map[file_extension]
            else:
                continue

            counter = 1
            while True:
                new_filename = f"{str(counter).zfill(5)}.txt"
                new_filepath = destination_folder / new_filename
                if not new_filepath.exists():
                    break
                counter += 1

            shutil.copy2(os.path.join(root, file), new_filepath)

destination_directory = "./data"
current_directory = "./"

for folder_name in os.listdir(current_directory):
    folder_path = os.path.join(current_directory, folder_name)
    
    if os.path.isdir(folder_path):
        organize_files(f"./{folder_name}", destination_directory)    


