#!/usr/bin/env python3
"""
def function
"""
from pymongo import MongoClient
from typing import List


def update_topics(mongo_collection: MongoClient,
                  name: str, topics: List[str]) -> str:
    """
    upddate data in database
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
