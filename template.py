import os, logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    # ------------- NOTEBOOKS ----------------------------
    f"notebooks/section01_pydantic.ipynb",
    
    "config/config.yaml",   # paths & settings
    "params.yaml",          # hyperparameters
    ".env",                 # secrets
    "requirements.txt",
    
    # IGNORES
    ".gitignore",
]

for file in list_of_files:
    file_path = Path(file)
    file_dir ,file_name = os.path.split(file_path)
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {file_name}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file_path} already exists")