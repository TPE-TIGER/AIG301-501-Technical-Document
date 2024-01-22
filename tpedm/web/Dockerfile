#----
FROM ubuntu:20.04
RUN apt update && apt install -y libpq-dev python3-pip gunicorn curl
COPY . /dm-web
WORKDIR /dm-web
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "-u" , "./web.py" ]
