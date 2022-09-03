FROM python:3.8.0-slim
WORKDIR /core
ADD . /core
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD gunicorn app:core --bind 0.0.0.0:$PORT --reload