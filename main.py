import os
import pdb
from flask import Flask, request
from qr.generate import GenerateQRCode
from PIL import Image

from gen_image.concat_image import ConcatImage

app = Flask(__name__)

FILE_UPLOADER_PATH = os.getenv('FILE_UPLOADER_PATH')
FILE_QR_PATH = os.getenv('FILE_QR_PATH')


@app.route("/generate_qr", methods=['POST'])
def generate_qr():
    data = request.get_json()
    url = data.get('url')
    version = 1
    box_size = 2
    border = 1

    user_exists = data.get("user_exists")
    user_name = data.get("user_name")
    path = data.get('path')

    qr_object = GenerateQRCode(url, version, box_size, border, user_exists, user_name, path)
    if qr_object.generate():
        return {'message': "qr saved", "status": 200}
    else:
        return {'message': 'failed', 'status': 400}


@app.route("/concat", methods=['POST'])
def concat_images():
    data = request.get_json()
    image_name = data.get('image')
    qr_name = data.get('qr')
    final_image_name = data.get("final_image_name")
    user_name = data.get('user_name')
    position = data.get('position')
    image = Image.open(f'{FILE_UPLOADER_PATH}/{user_name}/images/{os.path.basename(image_name["image_path"])}')
    qr_code = Image.open(f"{FILE_QR_PATH}/{user_name}/qrs/{os.path.basename(qr_name['path']) + '.png'}")

    concatenated = ConcatImage(qr_code, image, position, (300, 300), user_name,final_image_name)
    concatenated.generate_small()

    return 'success'


@app.route("/upload_image", methods=['POST'])
def upload_image():
    file = request.files['file']
    user_name = request.form.get("user_name")
    if file:
        file_path = os.path.join(FILE_UPLOADER_PATH, user_name, file.filename)
        file.save(file_path)
        return 'file saved!'


if __name__ == "__main__":
    app.run(debug=True)
