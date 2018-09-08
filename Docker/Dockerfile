FROM python:3.7.0-alpine3.8

LABEL maintainer="Evan Richardson"
LABEL version="1.1"

WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app/src/python
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
#RUN rm -rf /var/cache/apk

CMD ["/app/src/bin/tHome-eagle.py", "-c", "/app/src/conf"]

EXPOSE 22042
