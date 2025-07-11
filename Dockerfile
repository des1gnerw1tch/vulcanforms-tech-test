FROM python:3.12
RUN apt-get update && apt-get install -y libgl1 # For OpenCV need this system library

WORKDIR /app
COPY image_flask_app ./image_flask_app
RUN pip install --no-cache-dir -r ./image_flask_app/requirements.txt
EXPOSE 5000

CMD ["flask", "--app", "./image_flask_app/image_services.py", "run", "--host=0.0.0.0"]
