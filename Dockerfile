FROM python:3.7.2-slim
WORKDIR /superheroes
ADD requirements.txt requirements.txt
RUN pip install --upgrade pip &&\ 
    pip install -r requirements.txt &&\
    pip install gunicorn &&\
    pip install psycopg2-binary
ADD api api
ADD manage.py manage.py
ADD wsgi.py wsgi.py
ADD cmd.sh cmd.sh
RUN chmod a+x cmd.sh
ENTRYPOINT [ "/superheroes/cmd.sh" ]