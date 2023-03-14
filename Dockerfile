FROM python:3-slim-buster

RUN apt-get update && apt-get install -y \
    mariadb-server \
    cron \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

RUN service mysql start && \
    mysql -u root -e "CREATE DATABASE mydb" && \
    mysql -u root -e "CREATE USER 'user1'@'localhost' IDENTIFIED BY 'password@123'" && \
    mysql -u root -e "GRANT ALL PRIVILEGES ON mydb.* TO 'user1'@'localhost'"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt