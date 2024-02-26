# flask_server.py

# Import necessary libraries
import json
from datetime import datetime, timedelta
from flask import Flask, request

# Create a Flask application
app = Flask(__name__)

# Endpoint to check the health of the server
@app.route("/")
def health():
    return "OK"

# Endpoint to manage tickets
@app.route("/ticket", methods=["POST"])
def manage_tickets():
    # Extract story points from the request body
    points = json.loads(request.data).get("story_points")
    # Calculate the expected deadline based on the story points
    expected_deadline = datetime.utcnow() + timedelta(days=points)
    # Return the expected deadline as a string
    return expected_deadline.strftime("%Y-%m-%d %H:%M:%S")

# Entry point of the script
if __name__ == "__main__":
    # Run the Flask application
    app.run(port=3000)
