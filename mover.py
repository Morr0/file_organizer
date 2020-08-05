import os
import os.path
from pathlib import Path 

# Constants
DEFAULT = "Others"

def move_files(path: str):
    for filePath in os.listdir(path):
        if (os.path.isfile(filePath)):
            destDir = DEFAULT

            # Check whether the file is being used by another process, if so skip it
            # if (util.is_file_open(filePath)):
            #     continue

            # Split the file path to access the last . in it to find the relevant dir to store in
            file_ext = get_file_ext(filePath)
            if (file_ext):
                destDir = get_belonging_dir_name(file_ext)
            
            # Place the file in the new dir
            Path(destDir).mkdir(parents=True, exist_ok=True)
            try:
                os.replace("./{}".format(filePath), "./{}/{}".format(destDir, filePath))
            except FileNotFoundError: # In case of temporary files while downloading, those get removed
                pass
            except PermissionError: # Will assume the file is being used by another process
                pass


def get_belonging_dir_name(fileExtension: str):
    if (fileExtension == "png" or fileExtension == "jpg" or fileExtension == "jpeg" or fileExtension == "gif" or fileExtension == "svg"):
        return "Images"
    elif (fileExtension == "pdf" or fileExtension == "docx" or fileExtension == "doc" or fileExtension == "txt"):
        return "Documents"
    elif (fileExtension == "csv" or fileExtension == "xlsx"):
        return "Spreadsheets"
    elif (fileExtension == "exe" or fileExtension == "msi" or fileExtension == "jar"):
        return "Executables"
    elif (fileExtension == "zip" or fileExtension == "rar"):
        return "Compressed"
    else:
        return DEFAULT

def get_file_ext(filePath: str):
    splits = filePath.split(".")
    if (len(splits) > 0):
        return splits[-1]
    
    return None

def get_file_without_ext(filePath: str):
    return Path(filePath).stem