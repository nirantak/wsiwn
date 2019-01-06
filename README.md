# WSIWN

> *What Should I Watch Next?*

## Table of Contents

- [WSIWN](#wsiwn)
    - [Table of Contents](#table-of-contents)
    - [Local Installation](#local-installation)
    - [Technology Stack](#technology-stack)
    - [Working](#working)
    - [REST API Endpoints](#rest-api-endpoints)

## Local Installation

- Install Python 3.7 from [here](https://www.python.org/downloads/release/python-370/)
- Install SWI-Prolog from [here](http://www.swi-prolog.org/Download.html)

- Install environment

    ```shell
    $ pip install -U pip pipenv
    $ git clone https://github.com/nirantak/wsiwn.git && cd wsiwn
    $ pipenv install --dev
    $ pipenv run pre-commit install
    ```

- Start Project
    - Run web app

        ```shell
        $ pipenv run start
        ```

        or

    - Run Prolog

        ```shell
        $ swipl server/prolog/movies.pl
        $ swipl server/prolog/tv.pl
        ```

        Execute queries
        ```prolog
        ?- movie(X, Z).
        ?- movie(X, L, G, D, Y).

        ?- tv(X, Z).
        ?- tv(X, L, G, D, S, T).
        ```

        where

        - X: Output variable (byte string)
        - Z: Input Search term (str)
        - L: Language (str)
        - G: Genre (str)
        - D: Duration {short, avg, long}
        - Y: Year (int)
        - S: Number of Seasons (int)
        - T: Status {ended, airing}

## Technology Stack

- Language - [Python3](https://www.python.org)
- Logic Programming - [SWI-Prolog](http://www.swi-prolog.org)
- Python - SWI-Prolog Bridge - [GitHub](https://github.com/yuce/pyswip), [SWIPL](http://www.swi-prolog.org/contrib/)
- Framework - [Flask](https://palletsprojects.com/p/flask/)

## Working

- [Web Scraping](https://github.com/nirantak/wsiwn/blob/master/server/scripts/scraper.py) - Scrape a website to get top 100 movies and TV shows sorted by popularity. Results are here: [Movies](https://github.com/nirantak/wsiwn/blob/master/server/data/movies.txt), [TV Shows](https://github.com/nirantak/wsiwn/blob/master/server/data/tv.txt).
- [Fetch Data](https://github.com/nirantak/wsiwn/blob/master/server/scripts/seed_data.py#L15) - Fetch information from OMDB API about each record from previous step. Results are here: [Movies](https://github.com/nirantak/wsiwn/blob/master/server/data/movies.json), [TV Shows](https://github.com/nirantak/wsiwn/blob/master/server/data/tv.json).
- Write [Prolog Statements](https://github.com/nirantak/wsiwn/blob/master/server/scripts/seed_data.py#L49) - Write Prolog facts for each record from the previous step and add search queries. Results are here: [Movies](https://github.com/nirantak/wsiwn/blob/master/server/prolog/movies.pl), [TV Shows](https://github.com/nirantak/wsiwn/blob/master/server/prolog/tv.pl).

## REST API Endpoints

---
| Method[name] | URI                      | Description                                                                                                                            |
| ------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| GET[movies]  | /api/movies?query=string | Display Movies matching query string                                                                                                   |
| GET[tv]      | /api/tv?query=string     | Display TV shows matching query string                                                                                                 |
| POST[movies] | /api/movies              | Search Movies with params (at least 1): [language(str), genre(str), duration{short, avg, long}, year(int)]                             |
| POST[tv]     | /api/tv                  | Search TV shows with params (at least 1): [language(str), genre(str), duration{short, avg, long}, seasons(int), status{airing, ended}] |
---
