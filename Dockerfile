
FROM tiangolo/uwsgi-nginx-flask:python3.10

# copy the requirements file into the image
COPY ./app/requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

RUN pip install -r requirements.txt

# production environment
ENV ENVIRONMENT production

# copy code from current directory
COPY ./app /app
