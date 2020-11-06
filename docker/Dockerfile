FROM python:3.8.6-slim-buster
WORKDIR /BirthDayManager
COPY requirements.txt .
COPY Application/ Application/
COPY Db/ Db/
COPY Tests/  Tests/
COPY ./docker/docker_entrypoint.sh .
COPY env-setup.sh .
RUN pip install -r requirements.txt
RUN apt-get -y update
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN chmod +x *.sh
ENTRYPOINT ["./docker_entrypoint.sh"]
