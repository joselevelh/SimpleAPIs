#
FROM python:3.9

#
LABEL authors="JoseLevel"


WORKDIR /drakes_api

#
COPY ./requirements.txt /drakes_api/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /drakes_api/requirements.txt

#
COPY ./app /drakes_api/app

ENV HOST 0.0.0.0
#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]