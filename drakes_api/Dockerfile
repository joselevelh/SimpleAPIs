#
FROM python:3.9

#
LABEL authors="JoseLevel"

# Setting env variable via arg to be passed at container run time or build time
ARG MONGO_URI_ARG
ENV MONGO_URI=$MONGO_URI_ARG

RUN echo $MONGO_URI
#
WORKDIR /drakes_api

#
COPY ./requirements.txt /drakes_api/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /drakes_api/requirements.txt

#
COPY ./app /drakes_api/app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]