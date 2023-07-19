#!/usr/bin/env python3
"""writing strings to redis"""
import redis
from typing import Union, Callable, Optional
import uuid
import sys
Unionsbif = Union[str, bytes, int, float]


class Cache:
    """Cache class"""
    def __init__(self):
        """store and instance of redis clientas a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Unionsbif) -> str:
        """creates key id and stores data in redis"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Unionsbif:
        """convert the data back to the desired format"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_int(self: bytes) -> int:
        """parametrize Cache.get with the correct conversion function"""
        return int.from_bytes(self, sys.byteorder)

    def get_str(self: bytes) -> str:
        """parametrize Cache.get with the correct conversion function."""
        return self.decode("utf-8")
