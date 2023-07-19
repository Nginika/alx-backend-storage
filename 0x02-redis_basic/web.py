#!/usr/bin/env python3
"""implement a get_page function (prototype: def get_page(url: str) -> str:).
The core of the function is very simple. It uses the requests module
to obtain the HTML content of a particular URL and returns it."""
import redis
import requests

# Redis connection
r = redis.Redis()


def get_page(url: str) -> str:
    """ Check if the URL content is already cached"""
    cached_content = r.get(f"cached:{url}")
    if cached_content:
        # URL content found in cache, return it
        return cached_content.decode('utf-8')

    # If URL content is not in cache, fetch it
    response = requests.get(url)

    # Cache the content with an expiration time of 10 seconds
    r.setex(f"cached:{url}", 10, response.text)

    # Increment the count for the URL access
    r.incr(f"count:{url}")

    return response.text
