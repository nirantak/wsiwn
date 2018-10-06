# WSIWN

> *What Should I Watch Next?*

## Table of Contents

- [WSIWN](#wsiwn)
    - [Table of Contents](#table-of-contents)
    - [Local Installation](#local-installation)
    - [Technology Stack](#technology-stack)

## Local Installation

- Install Python 3.7 from [here](https://www.python.org/downloads/release/python-370/)
- Install SWI-Prolog from [here](http://www.swi-prolog.org/Download.html)
- Install [Pipenv](https://pipenv.readthedocs.io/en/latest/)

```shell
$ pip install -U pipenv
```

- Install environment

```shell
$ git clone https://github.com/nirantak/wsiwn.git && cd wsiwn
$ pipenv install --dev
```

- Run app

```shell
$ pipenv run start
```

## Technology Stack

- Language - [Python3](https://www.python.org)
- Logic Programming - [SWI-Prolog](http://www.swi-prolog.org)
- Framework - [Flask](https://palletsprojects.com/p/flask/)
