FROM python:alpine3.19

RUN apk update && apk add beep

RUN pip install Flask

COPY beep_server.py /app/beep_server.py

WORKDIR /app

CMD ["python", "beep_server.py"]