# server.py
# Import necessary libraries
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
import grpc

# Import generated Protocol Buffer classes
from definitions.builds.service_pb2 import Confirmation
from definitions.builds.service_pb2_grpc import TestServiceServicer, add_TestServiceServicer_to_server

# Get the absolute path of the directory this file is in
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define a class for implementing the gRPC service
class Service(TestServiceServicer):
    # Method to check the health of the service
    def Health(self, request, context):
        return request
    
    # Method to add a new ticket and return a confirmation
    def AddTicket(self, request, context):
        # Calculate the expected deadline based on the story points of the ticket
        expected_deadline = datetime.utcnow() + timedelta(days=request.story_points)
        # Return a confirmation with the expected deadline
        return Confirmation(expected_deadline=expected_deadline.strftime("%Y-%m-%d %H:%M:%S"))

# Function to execute the gRPC server
def execute_server():
    # Create a gRPC server
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    # Add the TestServiceServicer implementation to the server
    add_TestServiceServicer_to_server(Service(), server)
    # Add an insecure port for communication
    server.add_insecure_port('[::]:3000')
    # Start the server
    server.start()
    print("Server started")
    # Wait for the server to terminate
    server.wait_for_termination()

# Entry point of the script
if __name__ == '__main__':
    execute_server()
    print("Server started")
    print("Press Ctrl+C to stop the server")
    