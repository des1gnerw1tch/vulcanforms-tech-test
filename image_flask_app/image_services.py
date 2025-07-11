from flask import Flask, request, jsonify
import numpy as np
import cv2

app = Flask(__name__)

@app.route("/images/intensity", methods=['POST'])
def get_intensity_of_image():
    file = request.files.get('image')

    if (file is None):
        return jsonify({"error": "Missing image file. Make sure to include image file in the 'image' field of the POST request"}), 400
    
    img_file_bytes = np.frombuffer(file.read(), np.uint8)
    color = cv2.imdecode(img_file_bytes, cv2.IMREAD_COLOR)

    if (color is None):
        return jsonify({"error": "Error when decoding image, make sure image file is valid"}), 400
    
    gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)

    color_intensities = cv2.mean(color)
    response = jsonify({'average_intensity': cv2.mean(gray)[0], 
                        'average_intensity_blue': color_intensities[0],
                        'average_intensity_green': color_intensities[1],
                        'average_intensity_red': color_intensities[2]})
    return response, 200
