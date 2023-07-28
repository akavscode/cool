FROM python:3.8-slim

WORKDIR /app
COPY . .

RUN apt-get update -y && apt-get install -y curl &&\
    curl -fsSL https://deb.nodesource.com/setup_14.x | bash - &&\
    apt-get install -y nodejs &&\
    pip install --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# CMD ["sh", "-c", "gunicorn -b 0.0.0.0:8080 --workers 2 index:app"]
CMD ["python", "index.py"]