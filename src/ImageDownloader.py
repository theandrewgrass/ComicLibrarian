import os
from PIL import Image
import requests
from io import BytesIO


class ImageDownloader:

    def __init__(self):
        self.file_path = os.getcwd()

    def create_comics_folder(self):
        comics_folder = f'{self.file_path}\\Comics'
        if not os.path.exists(comics_folder):
            os.makedirs(comics_folder)

        self.file_path = comics_folder

    def download_image_as_byes(self, url):
        response = requests.get(url)
        img = Image.open(BytesIo(response.content))