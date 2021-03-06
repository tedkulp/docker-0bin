FROM python:3.7

WORKDIR /app

RUN python -m pip install zerobin --user

EXPOSE 80
VOLUME /data

CMD ["python", "-m", "zerobin", "--port", "80", "--host", "0.0.0.0", "--data-dir", "/data"]
