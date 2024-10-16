FROM ubuntu:24.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install pandas==2.2.2 --break-system-packages && \
    pip install pyarrow --break-system-packages

# Copy protobuf
COPY table.proto /table.proto

# Run protobuff
RUN pip3 install grpcio-tools==1.66.1 grpcio==1.66.1 protobuf==5.27.2 --break-system-packages

# Copy remaining files
COPY *.py /
COPY *.csv /

# Default command to run the server
CMD ["python3", "-u", "server.py"]

