FROM python:slim

WORKDIR /usr/src/path

COPY ibdatastream ibdatastream
COPY setup.py setup.py
COPY LICENSE LICENSE
COPY README.md README.md
RUN pip install --no-cache-dir .

CMD python -m ibdatastream