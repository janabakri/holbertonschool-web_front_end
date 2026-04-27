#!/usr/bin/env python3
"""Nginx log stats script"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total logs
    print("{} logs".format(collection.count_documents({})))

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {m: 0 for m in methods}

    # Aggregate method counts
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]

    for doc in collection.aggregate(pipeline):
        if doc["_id"] in method_counts:
            method_counts[doc["_id"]] = doc["count"]

    for m in methods:
        print("\tmethod {}: {}".format(m, method_counts[m]))

    # GET /status
    status_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    print("{} status check".format(status_count))
