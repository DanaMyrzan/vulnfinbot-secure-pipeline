
FROM python:3.12-slim

WORKDIR /app

# Update system packages
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

COPY run.py .

EXPOSE 5000

CMD ["python", "run.py"]
