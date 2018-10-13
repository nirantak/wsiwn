from typing import List

from pyswip import Prolog


def search(swipl: Prolog, category: str, query: str) -> List[str]:
    """Query the knowledge-base for given string and return list of matches"""

    q = swipl.query(f"{category}(X, {query})")
    result = [i["X"].decode("utf-8") for i in list(q)]

    return result


def advance_search():
    pass
