#----
FROM ubuntu:20.04
#RUN apt update && apt install -y libpq-dev python3-pip gunicorn
RUN apt update && apt install -y libpq-dev python3-pip

COPY . /dm-postgresql
WORKDIR /dm-postgresql

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "-u" , "./initDatabase.py" ]

