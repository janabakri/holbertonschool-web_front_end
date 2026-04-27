#!/usr/bin/env python3
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nginx = client.logs.nginx

print("{} logs".format(nginx.count_documents({})))
print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    count = nginx.count_documents({"method": method})
    print("\tmethod {}: {}".format(method, count))

print("{} status check".format(
    nginx.count_documents({"method": "GET", "path": "/status"})
))
