# Pull official base image 
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev libmagic1 libffi-dev netcat-traditional \
    && pip install Pillow

# Install git
RUN apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY ./app/requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

# Copy entrypoint.sh
COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

COPY ./app /app

ENTRYPOINT [ "/entrypoint.sh" ]