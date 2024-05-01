#!/usr/bin/env python3
""" redis task """

from functools import wraps
import redis
import requests
from typing import Callable

_redis = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ count """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ wrapper function """
        _redis.incr(f"count:{url}")
        cached = _redis.get(f"cached:{url}")
        if cached:
            return cached.decode('utf-8')
        html = method(url)
        _redis.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ req url """
    req = requests.get(url)
    return req.text
