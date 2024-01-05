FROM python:3.11.7-bookworm

RUN apt update
RUN apt install build-essential -y

RUN pip3 install pyvoronoi
# RUN python3 -m pip install --index-url https://test.pypi.org/simple/ pyvoronoi --no-cache-dir

COPY test.py test.py
CMD ["test.py"]
ENTRYPOINT ["python3"]