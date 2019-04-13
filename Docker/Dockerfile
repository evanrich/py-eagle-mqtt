FROM python:3.7.3-alpine3.9

LABEL maintainer="Evan Richardson"
LABEL version="1.4"

WORKDIR /app
COPY . /app
COPY ./src/conf/logrotate/tHome /etc/logrotate.d/
ENV PYTHONPATH=/app/src/python
RUN apk --update add --no-cache logrotate \
&& pip3 install --no-cache-dir  --upgrade pip \
&& pip3 install --no-cache-dir -r requirements.txt
#RUN rm -rf /var/cache/apk

CMD ["/app/src/bin/tHome-eagle.py", "-c", "/app/src/conf"]

EXPOSE 22042
