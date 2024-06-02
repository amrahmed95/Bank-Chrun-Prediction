# Update Components

import os
import requests
import urllib.request as request
from pathlib import Path
import zipfile
from src.BankChurn import logger
from src.BankChurn.utils.common import get_size
from src.BankChurn.config.configuration import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        local_file = Path(self.config.local_data_file)

        if not local_file.exists():
            response = requests.get(self.config.source_URL, stream=True)

            if response.status_code == 200:
                with local_file.open(mode='wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)

                logger.info(f"{local_file.name} downloaded with headers: \n{response.headers}")
            else:
                logger.error(f"Failed to download file from {self.config.source_URL}")
        else:
            file_size = get_size(local_file)
            logger.info(f"File already exists of size: {file_size}")



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
  