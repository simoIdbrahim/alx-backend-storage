#!/usr/bin/env python3
"""
def function
"""
from typing import List
from pymongo import MongoClient


def schools_by_topic(mongo_collection: MongoClient,
                     topic: str) -> List[object]:
    """
    fetch data
    """
    return mongo_collection.find({"topics": topic})
