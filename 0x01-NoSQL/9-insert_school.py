#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based on kwargs:
Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
"""
import sys


def insert_school(mongo_collection, **kwargs):
    """inserts new document in a collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
