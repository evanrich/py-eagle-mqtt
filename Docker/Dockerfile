FROM python:2.7.15-alpine3.8

LABEL maintainer="Evan Richardson"
LABEL version="1.0"

WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app/src/python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm -rf /var/cache/apk

CMD ["/app/src/bin/tHome-eagle.py", "-c", "/app/src/conf"]

EXPOSE 22042
