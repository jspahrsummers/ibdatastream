FROM python:slim

WORKDIR /usr/src/path

COPY ibdatastream ibdatastream
COPY setup.py setup.py
COPY LICENSE LICENSE
COPY README.md README.md
RUN pip install --no-cache-dir .

EXPOSE 50051
ENTRYPOINT [ "ibdatastream", "--port", "50051" ]