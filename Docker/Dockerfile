FROM python:3.9.4-alpine3.13
LABEL maintainer="Evan Richardson (evanrich81[at]gmail.com)"

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.name="evanrich/py-eagle-mqtt"
LABEL org.label-schema.description="Python Rainforest Eagle to MQTT Application"
LABEL org.label-schema.vcs-url="https://github.com/evanrich/py-eagle-mqtt"
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vendor="Evan Richardson"
LABEL org.label-schema.docker.cmd="docker run --name=py-eagle-mqtt -e MQTT_BROKER_IP=<IP> -e MQTT_BROKER_PORT=1883 -p 22042:22042 -d evanrich/py-eagle-mqtt"

WORKDIR /app
COPY requirements.txt /app
COPY ./src/conf/logrotate/tHome /etc/logrotate.d/
ENV PYTHONPATH=/app/src/python
RUN apk --update add --no-cache logrotate \
&& pip3 install --no-cache-dir  --upgrade pip \
&& pip3 install --no-cache-dir -r requirements.txt
COPY . /app
CMD ["/app/src/bin/tHome-eagle.py", "-c", "/app/src/conf"]

EXPOSE 22042
