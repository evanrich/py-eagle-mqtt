FROM python:3.9.4-alpine3.13

LABEL maintainer="Evan Richardson (evanrich81[at]gmail.com)"
#LABEL version="1.7.0"

WORKDIR /app
COPY . /app
COPY ./src/conf/logrotate/tHome /etc/logrotate.d/
ENV PYTHONPATH=/app/src/python
RUN apk --update add --no-cache logrotate \
&& pip3 install --no-cache-dir  --upgrade pip \
&& pip3 install --no-cache-dir -r requirements.txt

CMD ["/app/src/bin/tHome-eagle.py", "-c", "/app/src/conf"]

EXPOSE 22042
