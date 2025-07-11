import pytest
import json
from image_services import app
import os
import math

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


# Test do not give file in POST request
def test_missing_file(client):
    response = client.post("/images/intensity")
    assert response.status_code == 400
    assert response.get_json() == {'error': "Missing image file. Make sure to include image file in the 'image' field of the POST request"}


# Test give file but not an image file
def test_non_image_file(client):
    file_path = os.path.join(os.path.dirname(__file__), 'images', 'textFile.txt')
    with open(file_path, 'rb') as image_file:
        data = {
            'image': (image_file, 'textFile.txt')
        }
        response = client.post('/images/intensity', data=data, content_type='multipart/form-data')
        assert response.status_code == 400
        assert response.get_json() == {"error": "Error when decoding image, make sure image file is valid"}


# Test give valid image and that intensities are correct
def test_valid_image_file(client):
    file_path = os.path.join(os.path.dirname(__file__), 'images', 'savingPunyville.jpg')
    with open(file_path, 'rb') as image_file:
        data = {
            'image': (image_file, 'savingPunyville.jpg')
        }
        response = client.post('/images/intensity', data=data, content_type='multipart/form-data')
        assert response.status_code == 200
        result_intensities = response.get_json()
        assert math.isclose(result_intensities['average_intensity'], 125.7984, abs_tol=0.001)
        assert math.isclose(result_intensities['average_intensity_blue'], 50.3556, abs_tol=0.001)
        assert math.isclose(result_intensities['average_intensity_green'], 147.6010, abs_tol=0.001)
        assert math.isclose(result_intensities['average_intensity_red'], 111.8956, abs_tol=0.001)


