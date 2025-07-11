
from flask import Flask, request
import numpy as np
import cv2

app = Flask(__name__)

@app.route("/")
def test():
    return "Hello World!"


@app.route("/images/intensity", methods=['POST'])
def get_intensity_of_image():
    print(request.files)
    file = request.files.get('image')
    img_file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_file_bytes, cv2.IMREAD_COLOR)

    blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite('blurred.jpg', blurred_img)
    return file.filename
