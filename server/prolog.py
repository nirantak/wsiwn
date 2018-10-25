from textwrap import dedent
from typing import Any, Dict, Iterable, List

from pyswip import Prolog


def search(swipl: Prolog, category: str, query: str) -> List[str]:
    """
    Query the knowledge-base for given string and return list of matches
    """

    result: Iterable[Dict[str, Any]] = swipl.query(f"{category}(X, {query})")
    res = [
        i["X"].decode(encoding="utf-8", errors="backslashreplace") for i in list(result)
    ]

    return res


def advance_search(
    swipl: Prolog, category: str, query: Dict[str, str]
) -> List[Dict[str, Any]]:
    """
    Query the knowledge-base for all input query parameters
    and return list of matches
    """

    q: str = ""
    data: Dict[str, str] = {}

    for k, v in query.items():
        if type(v) is str:
            v = v.lower()
            if v.isdecimal():
                v = int(v)
        data[k] = v

    if category == "movies":
        q = dedent(
            f"""
            movies( Movie,
                    {data.get('language') or 'Language'},
                    {data.get('genre') or 'Genre'},
                    {data.get('duration') or 'Duration'},
                    {data.get('year') or 'Year'}
                ).
            """
        )
    elif category == "tv":
        q = dedent(
            f"""
            tv( Tv,
                {data.get('language') or 'Language'},
                {data.get('genre') or 'Genre'},
                {data.get('duration') or 'Duration'},
                {data.get('seasons') or 'Seasons'},
                {data.get('status') or 'Status'}
            ).
            """
        )
    else:
        return "Invalid category!"

    result: Iterable[Dict[str, Any]] = swipl.query(q)
    # result = [
    #     i["X"].decode(encoding="utf-8", errors="backslashreplace") for i in list(q)
    # ]

    res = [
        dict(
            (
                k,
                v.decode(encoding="utf-8", errors="backslashreplace")
                if type(v) is bytes
                else v,
            )
            for k, v in i.items()
        )
        for i in list(result)
    ]

    return res
