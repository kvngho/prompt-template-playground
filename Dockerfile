FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt update
RUN apt install default-jdk -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .