#!/usr/bin/env python3
"""Module to update school topics"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of school documents based on the name.

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to match
        topics (list): list of topics to set
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
