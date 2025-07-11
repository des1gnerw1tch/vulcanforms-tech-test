FROM python:3.12
RUN apt-get update && apt-get install -y libgl1 # For OpenCV need this system library

WORKDIR /app
COPY src ./src
RUN pip install --no-cache-dir -r ./src/requirements.txt
EXPOSE 5000

CMD ["flask", "--app", "./src/average-intensity-of-image.py", "run", "--host=0.0.0.0"]
