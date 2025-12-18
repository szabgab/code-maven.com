FROM ubuntu:25.10
RUN apt update && \
    apt install -y cron

COPY crontab.txt /opt
RUN crontab /opt/crontab.txt

CMD ["cron", "-f"]
