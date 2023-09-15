# Gunakan image resmi Python
FROM python:3.9-slim

# Atur variabel lingkungan
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instal dependensi yang diperlukan
RUN apt-get update && \
    apt-get install -y gcc python3-dev libpq-dev

# Pasang dependensi
RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Set direktori kerja di container
WORKDIR /app

# Copy seluruh proyek ke direktori kerja container
COPY . /app/

CMD ["gunicorn", "FavShop.wsgi:application", "--bind", "0.0.0.0:8000"]
