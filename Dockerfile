FROM python:3.12
WORKDIR /app
COPY src ./src
RUN pip install --no-cache-dir -r ./src/requirements.txt
EXPOSE 5000

CMD ["flask", "--app", "./src/average-intensity-of-image.py", "run", "--host=0.0.0.0"]
