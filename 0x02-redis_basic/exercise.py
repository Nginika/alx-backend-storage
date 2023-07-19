#/usr/bin/env python3
"""writing strings to redis"""
import redis


class Cache:
    def __init__(self):
        """store and instance of redis clientas a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

