#!/usr/bin/env python3
"""writing strings to redis"""
import redis
from typing import Union
import uuid


class Cache:
    """Cache class"""
    def __init__(self):
        """store and instance of redis clientas a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """creates key id and stores data in redis"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key
