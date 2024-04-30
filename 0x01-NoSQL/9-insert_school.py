#!/usr/bin/env python3
"""
deffunction
"""
from pymongo import MongoClient
from typing import Mapping


def insert_school(mongo_collection: MongoClient,
                  **kwargs: Mapping[str, str]) -> str:
    """
    add data to database
    """
    return mongo_collection.insert_one(kwargs).inserted_id
