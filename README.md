# vulcanforms-tech-test

Steps to run service:
1. Have Docker installed
2. Build image in root directory where Dockerfile is: sudo docker build -t tech-test . 
3. Run container and map ports: sudo docker run --rm -p 5000:5000 tech-test
4. In another terminal window, feed image into service: curl -X POST -F "image=@PATH_TO_FILE" http://127.0.0.1:5000/images/intensity

Steps to run unit tests:
1. Follow steps 1 and 2 above
2. Run pytest unit tests: sudo docker run --rm tech-test pytest

I included 3 tests for basic coverage. It would be good to add more tests and edge cases if we wanted to fully flesh out the service.

* Test 1: Make sure that error is handled and correct error message is returned if submit POST request with no image file to service.

* Test 2: Make sure that error is handled and correct error message is returned if submit POST request with a file, but the file is not an image file (in our case, it is a .txt file)

* Test 3: Make sure that correct average intensities are returned when send POST request with valid jpg image.

I used OpenCV for image processing, so it should be able to handle multiple different image file formats. In the unit tests I use jpg. 
