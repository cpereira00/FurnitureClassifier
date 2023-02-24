FROM python:3.9-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "80"]