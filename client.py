# client.py

# Import necessary libraries
from time import time
import grpc

# Import generated Protocol Buffer classes
from definitions.builds.service_pb2 import Null, Ticket
from definitions.builds.service_pb2_grpc import TestServiceStub

# Function to send requests to the gRPC server
def main():
    # Establish a connection to the gRPC server
    with grpc.insecure_channel('localhost:3000') as channel:
        # Create a gRPC client stub
        client = TestServiceStub(channel)
        # Check the health of the service
        client.Health(Null())
        # Record the start time
        start = time()
        
        # Send 2000 requests to the server
        for _ in range(2000):
            # Create a ticket and add it to the server
            confirmation = client.AddTicket(Ticket(
                name="TestTicket",
                description="TestDescription",
                story_points=2
            ))

        # Print the expected deadline from the last confirmation
        print(confirmation.expected_deadline)
        # Print the time taken to send 2000 requests
        print(time() - start)

# Entry point of the script
if __name__ == '__main__':
    main()
    