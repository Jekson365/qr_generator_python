import random

import qrcode
from dotenv import load_dotenv
import os

load_dotenv()

FILE_QR_PATH = os.getenv('FILE_QR_PATH')

class GenerateQRCode:
    def __init__(self, url, version, box_size, border,user_exits,user_name,path):
        self.url = url
        self.version = version
        self.box_size = box_size
        self.border = border
        self.user_exits = user_exits
        self.user_name = user_name
        self.path = path

    def generate(self):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=self.box_size,
            border=self.border
        )

        qr.add_data(self.url)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        if not self.user_exits:
            os.mkdir(f'{FILE_QR_PATH}/{self.user_name}')
            img.save(f"{FILE_QR_PATH}/{self.user_name}/qrs/{self.path}.png")
            return True
        else:
            img.save(f"{FILE_QR_PATH}/{self.user_name}/qrs/{self.path}.png")
            return True
