FROM python:3.8-slim


RUN apt update
RUN apt install build-essential -y

RUN pip3 install pyvoronoi


COPY test.py test.py
CMD ["test.py"]
ENTRYPOINT ["python3"]