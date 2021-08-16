FROM alpine:latest
RUN apk add python3 py3-pip
RUN pip install flask
WORKDIR /opt
COPY app.py .
CMD ["flask", "run", "--host", "0.0.0.0"]
