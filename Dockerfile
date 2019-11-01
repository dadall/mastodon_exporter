FROM alpine

RUN mkdir -p /app/instance_exporter

WORKDIR /app/instance_exporter

COPY requirements.txt /app/instance_exporter
RUN apk add --no-cache python3 && python3 -m ensurepip && pip3 install --upgrade pip setuptools 
RUN pip3 install --no-cache-dir -r requirements.txt

COPY instance_exporter.py /app/instance_exporter

EXPOSE 9410

ENTRYPOINT [ "python3", "./instance_exporter.py"]

