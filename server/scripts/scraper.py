import os
from typing import Set, Tuple

import requests
from bs4 import BeautifulSoup

from server import PROJECT_ROOT

URL_MOVIES: str = os.environ["URL_MOVIES"]
URL_TV: str = os.environ["URL_TV"]


def get_watchlist(pages: int = 5) -> Tuple[Set[str], Set[str]]:
    """
    Get a tuple containing two sets: a set of movies, and a set of TV shows,
    with 20*pages entries each
    """
    movies: Set[str] = set()
    tv: Set[str] = set()

    for page in range(pages):
        req_mv = requests.get(URL_MOVIES, params={"page": page})
        req_tv = requests.get(URL_TV, params={"page": page})

        soup_mv = BeautifulSoup(req_mv.content, "html.parser")
        soup_tv = BeautifulSoup(req_tv.content, "html.parser")

        data_mv = soup_mv.find_all("p", {"class": "view_more"})
        data_tv = soup_tv.find_all("p", {"class": "view_more"})

        movies.update({m.a["title"] for m in data_mv})
        tv.update({t.a["title"] for t in data_tv})

        req_mv.close()
        req_tv.close()

    return movies, tv


if __name__ == "__main__":
    movies, tv = get_watchlist(6)

    with open(os.path.join(PROJECT_ROOT, "data/movies_list.txt"), "w") as fm:
        for m in movies:
            fm.write(f"{m}\n")

    with open(os.path.join(PROJECT_ROOT, "data/tv_list.txt"), "w") as ft:
        for t in tv:
            ft.write(f"{t}\n")

    print(f"Fetched top popular {len(movies)} movies and {len(tv)} TV shows")
