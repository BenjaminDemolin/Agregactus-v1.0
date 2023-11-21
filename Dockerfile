FROM python:3.10

WORKDIR /Agregactus

COPY . /Agregactus/

RUN pip install -r requirements.txt

CMD ["python", "/Agregactus/main.py"]
