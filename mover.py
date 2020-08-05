import os
import os.path
from pathlib import Path 

# Constants
DEFAULT = "Others"

def move_files(path: str):
    for filePath in os.listdir(path):
        if (os.path.isfile(filePath)):
            destDir = DEFAULT

            # Split the file path to access the last . in it to find the relevant dir to store in
            splits = filePath.split(".")
            if (len(splits) > 0):
                destDir = get_belonging_dir_name(splits[-1])
            
            # Place the file in the new dir
            Path(destDir).mkdir(parents=True, exist_ok=True)
            os.rename("./{}".format(filePath), "./{}/{}".format(destDir, filePath))


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
    