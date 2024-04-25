###########
# BUILDER #
###########

# base image
FROM python:3.10-slim-buster as builder

# pwd
WORKDIR /usr/src/backend

# env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# install deps
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/backend/wheels -r requirements.txt

#########
# FINAL #
#########

# base image
FROM python:3.10-slim-buster

# create directory for app user
RUN mkdir -p /home/getit

# create app user
RUN addgroup --system getit && adduser --system --group getit

# create directories
ENV HOME=/home/getit
ENV APP_HOME=/home/getit/backend
RUN mkdir $APP_HOME

RUN mkdir $APP_HOME/static
RUN chown getit: $APP_HOME/static
RUN chmod u+w $APP_HOME/static

RUN mkdir $APP_HOME/media
RUN chown getit: $APP_HOME/media
RUN chmod u+w $APP_HOME/media
WORKDIR $APP_HOME

# install deps
RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/backend/wheels /wheels
COPY --from=builder /usr/src/backend/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# copy project
COPY . $APP_HOME

# change user
USER getit

# run entrypoint.sh
ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]
