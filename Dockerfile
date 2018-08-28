FROM python:2.7.15-alpine3.8

LABEL maintainer="Evan Richardson"
LABEL version="1.0"

WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app/src/python
RUN pip install -r requirements.txt
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc python-dev build-base 
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip install --no-cache-dir numpy
RUN rm -rf /var/cache/apk

CMD ["/app/src/bin/tHome-eagle.py", "-c", "/app/src/conf"]

EXPOSE 22042
