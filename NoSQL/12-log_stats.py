#!/usr/bin/env python3
"""
Log stats script that provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def log_stats():
    """
    Connects to MongoDB and prints statistics about the nginx collection.
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    
    # Get total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Print Methods section
    print("Methods:")
    
    # Define methods in the required order
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    # Count and print each method
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Count GET requests to /status path
    status_check_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
