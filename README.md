# WSIWN

> *What Should I Watch Next?*

## Table of Contents

- [WSIWN](#wsiwn)
    - [Table of Contents](#table-of-contents)
    - [Local Installation](#local-installation)
    - [Technology Stack](#technology-stack)
    - [Working](#working)

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

- Start Project
    - Run web app

        ```shell
        $ pipenv run start
        ```

        or

    - Run Prolog

        ```shell
        $ swipl prolog/movies.pl
        $ swipl prolog/tv.pl
        ```

        Execute queries
        ```prolog
        ?- movie(X, Z).
        ?- movie(X, L, G, D, Y).

        ?- tv(X, Z).
        ?- tv(X, L, G, D, S, T).
        ```

        where

        - X: Output variable
        - Z: Input Search term
        - L: Language
        - G: Genre
        - D: Duration (short, avg, long)
        - Y: Year
        - S: Number of Seasons
        - T: Status (ended, airing)

## Technology Stack

- Language - [Python3](https://www.python.org)
- Logic Programming - [SWI-Prolog](http://www.swi-prolog.org)
- Python - SWI-Prolog Bridge - [GitHub](https://github.com/yuce/pyswip), [SWIPL](http://www.swi-prolog.org/contrib/)
- Framework - [Flask](https://palletsprojects.com/p/flask/)

## Working

- [Web Scraping](https://github.com/nirantak/wsiwn/blob/master/scripts/scraper.py) - Scrape a website to get top 100 movies and TV shows sorted by popularity. Results are here: [Movies](https://github.com/nirantak/wsiwn/blob/master/data/movies_list.txt), [TV Shows](https://github.com/nirantak/wsiwn/blob/master/data/tv_list.txt).
- [Fetch Data](https://github.com/nirantak/wsiwn/blob/master/scripts/seed_data.py) - Fetch information from OMDB API about each record from previous step. Results are here: [Movies](https://github.com/nirantak/wsiwn/blob/master/data/movies.json), [TV Shows](https://github.com/nirantak/wsiwn/blob/master/data/tv.json).
- Write [Prolog Statements](https://github.com/nirantak/wsiwn/blob/master/scripts/seed_data.py#L47) - Write Prolog facts for each record from the previous step and add search queries. Results are here: [Movies](https://github.com/nirantak/wsiwn/blob/master/prolog/movies.pl), [TV Shows](https://github.com/nirantak/wsiwn/blob/master/prolog/tv.pl).
