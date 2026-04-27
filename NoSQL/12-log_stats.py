#!/usr/bin/env python3
"""Nginx log stats script"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total logs
    print("{} logs".format(collection.count_documents({})))

    # Methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        print("\tmethod {}: {}".format(
            m, collection.count_documents({"method": m})
        ))

    # Status check
    print("{} status check".format(
        collection.count_documents({
            "method": "GET",
            "path": "/status"
        })
    ))
