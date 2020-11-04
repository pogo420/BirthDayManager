FROM python:3.8.6-slim-buster
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY Application/ .
COPY Db/ .
COPY Tests/ .
RUN . ./env-setup.sh
CMD ["python3", "-m", "flask", "run"]

