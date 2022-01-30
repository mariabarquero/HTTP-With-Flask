FROM alpine:3.15.0

RUN apk add --no-cache python3-dev build-base libffi-dev \
    && apk add --no-cache py3-pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "src/server.py"]
