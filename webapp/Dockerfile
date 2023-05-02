FROM python:3.7.9-alpine


WORKDIR /app
COPY . .

RUN pip install --upgrade pip setuptools

#no cache dir for downloading the packges from the interent without relying on the copies on the machine - after problem with flask-cores
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0"]