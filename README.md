# vulcanforms-tech-test
This is a microservice that calculates the average intensity of an image using Flask, Python, OpenCV, and Docker. An image from the users local filesystem can be sent to the service using a POST request. The JSON response includes the average intensity of the whole image by converting it to a grayscaled image first. The response also includes average intensities of the blue channel, green channel, and red channel.

An example JSON response from the service is this
``` {"average_intensity":125.83838220424671,"average_intensity_blue":50.513852376137514,"average_intensity_green":147.59502527805864,"average_intensity_red":111.93362992922144} ```

## Steps to run service:
1. Have Docker installed
2. Build image in root directory where Dockerfile is: ```sudo docker build -t tech-test . ```
3. Run container and map ports: ```sudo docker run --rm -p 5000:5000 tech-test```
4. In another terminal window, feed an image into service: ```curl -X POST -F "image=@PATH_TO_FILE" http://127.0.0.1:5000/images/intensity```

## Steps to run unit tests:
1. Follow steps 1 and 2 above
2. Run pytest tests: ```sudo docker run --rm tech-test pytest```

## Notes
I included 3 tests for basic coverage. It would be a good idea to add more tests and edge cases if we wanted to fully flesh out the service.

* Test 1: Make sure that error is handled and correct error message is returned if submit POST request with no image file to service.

* Test 2: Make sure that error is handled and correct error message is returned if submit POST request with a file, but the file is not an image file (in our case, it is a .txt file)

* Test 3: Make sure that correct average intensities are returned when send POST request with valid jpg image.

I used OpenCV for image processing, so it can handle multiple different image file formats. In the unit tests I use jpg. 
