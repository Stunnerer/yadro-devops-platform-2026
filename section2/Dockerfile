FROM ubuntu:22.04

RUN apt update && \
    apt install -y python3 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY script.py .

CMD ["python3", "script.py"]