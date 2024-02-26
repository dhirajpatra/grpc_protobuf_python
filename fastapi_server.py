# fastapi_server.py

# Import necessary libraries
import json
from datetime import datetime, timedelta

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request

# Create a FastAPI application
app = FastAPI()

# Endpoint to check the health of the server
@app.get("/health")
def health():
    return {"Hello": "World"}

# Endpoint to manage tickets
@app.post("/ticket")
async def manage_tickets(request: Request,):
    # Extract story points from the request body
    points = json.loads(await request.body()).get("story_points")
    # Calculate the expected deadline based on the story points
    expected_deadline = datetime.utcnow() + timedelta(days=points)
    # Return the expected deadline as a string
    return expected_deadline.strftime("%Y-%m-%d %H:%M:%S")

# Entry point of the script
if __name__ == "__main__":
    # Run the FastAPI application using uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
