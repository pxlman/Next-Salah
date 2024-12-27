# Start with a Python base image
FROM python:3.10-slim

# Set a working directory
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "main.py"]
