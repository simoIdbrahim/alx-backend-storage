#!/usr/bin/env python3
"""
def function
"""
from typing import Iterator
from pymongo import MongoClient


def top_students(mongo_collection: MongoClient) -> Iterator:
    """
    function that returns all students sorted by average score
    """
    return mongo_collection.aggregate([
        {'$addFields': {'averageScore': {'$avg': "$topics.score"}}},
        {'$sort': {'averageScore': -1}}
    ])
