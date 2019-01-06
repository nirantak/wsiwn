FROM python:3.7.2-slim

LABEL Name="wsiwn" maintainer="Nirantak Raghav"

RUN apt update && \
    apt install -qq -y software-properties-common --no-install-recommends && \
    apt-add-repository ppa:swi-prolog/stable
RUN echo "deb http://ppa.launchpad.net/swi-prolog/stable/ubuntu artful main" > /etc/apt/sources.list.d/swi-prolog-ubuntu-stable*.list && \
    apt install -qq -y swi-prolog --no-install-recommends
RUN python3 -m pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pipenv install --ignore-pipfile

COPY server /app/server

EXPOSE 5000
CMD ["pipenv", "run", "prod"]
