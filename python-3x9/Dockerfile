FROM python:3.9-slim


RUN apt update
RUN apt install build-essential -y

RUN pip3 install pyvoronoi
# RUN python3 -m pip install --index-url https://test.pypi.org/simple/ pyvoronoi --no-cache-dir

COPY test.py test.py
CMD ["test.py"]
ENTRYPOINT ["python3"]