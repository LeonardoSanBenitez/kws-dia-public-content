FROM arm64v8/python:3.7-slim-buster

WORKDIR /src

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-u", "./main.py" ]
