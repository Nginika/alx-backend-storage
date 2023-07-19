#!/usr/bin/env python3
"""implementing an expiring web cache and tracker"""
import requests
import redis
from typing import Dict

redis_client = redis.Redis()


def get_page(url: str) -> str:
    """ Check if the URL content is already cached"""
    cached_content = redis_client.get(url)
    if cached_content:
        # URL content found in cache, return it
        return cached_content.decode('utf-8')

    # If URL content is not in cache, fetch it
    response = requests.get(url)

    # Track the number of times the URL was accessed
    url_count_key = f"count:{url}"
    redis_client.incr(url_count_key)

    # Cache the content with an expiration time of 10 seconds
    redis_client.setex(url, 10, response.text)

    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
