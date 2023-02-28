FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code
RUN apt update && apt install telnet -y
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt