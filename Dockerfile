FROM python:3.11-slim

WORKDIR /app
COPY . /app
RUN python -m pip install -r requirements.txt

EXPOSE 8080:8080
ENTRYPOINT python -m uvicorn --reload --host 0.0.0.0 --port 8080 src.app:app