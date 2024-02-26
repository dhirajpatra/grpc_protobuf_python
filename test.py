# test.py

# Import necessary libraries
import json
from time import time
import urllib3

# Create a PoolManager instance to manage connections
http = urllib3.PoolManager()

# Function to send 2000 POST requests to the server
def main():
    # Record the start time
    start = time()

    # Send 2000 POST requests to the server
    for _ in range(2000):
        http.request(
            "POST",
            "http://localhost:3000/ticket",
            headers={"Content-Type": "application/json"},
            body=json.dumps({
                "name": "x",
                "description": "...",
                "story_points": 3
            })
        )

    # Print the time taken to send 2000 requests
    print(time() - start)

# Entry point of the script
if __name__ == "__main__":
    main()
