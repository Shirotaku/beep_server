FROM python:alpine3.19

RUN apt-get update && apt-get install -y beep

RUN pip install Flask

COPY beep_server.py /app/beep_server.py

WORKDIR /app

CMD ["python", "beep_server.py"]
