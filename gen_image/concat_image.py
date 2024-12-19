from PIL import Image
import os

FILE_CONCAT_PATH = os.getenv('FILE_CONCAT_PATH')


class ConcatImage:
    def __init__(self, qr_code, img, position, qr_size, user_name, final_image_name):
        self.qr_code = qr_code
        self.img = img
        self.position = position
        self.qr_size = qr_size
        self.final_image_name = final_image_name
        self.user_name = user_name

    def generate_small(self):
        new_width = 1500
        new_height = 1500

        new_image = Image.new('RGB', (new_width, new_height))

        self.img = self.img.resize((new_width, new_height))

        new_image.paste(self.img, (0, 0))
        self.qr_code = self.qr_code.resize(self.qr_size)
        self.place_qr_code(new_image, new_width, new_height)

        new_image.save(f'{FILE_CONCAT_PATH}/{self.user_name}/final/{self.final_image_name}.jpg')

    def place_qr_code(self, image, w, h):
        margin = 50

        if self.position == 'top-left':
            x = margin
            y = margin
        elif self.position == 'top-right':
            x = w - self.qr_size[0] - margin
            y = margin
        elif self.position == 'bottom-left':
            x = margin
            y = h - self.qr_size[1] - margin
        elif self.position == 'bottom-right':
            x = w - self.qr_size[0] - margin
            y = h - self.qr_size[1] - margin
        else:
            x = w - self.qr_size[0] - margin
            y = h - self.qr_size[1] - margin

        # Paste the QR code at the calculated coordinates
        image.paste(self.qr_code, (x, y))
