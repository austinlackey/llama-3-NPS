# Dockerfile, Image, Container
FROM python:3.11

ADD mlxModel.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./mlxModel.py" ]