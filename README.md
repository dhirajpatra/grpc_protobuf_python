# GRPC Protobuf Python Application

This application demonstrates the usage of gRPC (Google Remote Procedure Call) with Protocol Buffers in a Python environment. It includes server-side and client-side implementations using Protocol Buffers for message serialization and deserialization.

Also I am showing here to comparison of efficiency between different types of MVC farmework eg. Flask and FastAPI

## Installation and Setup

1. Clone the repository:
   `git clone <repository_url>`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Generate gRPC stubs:

Run the bellow command from your root directory to create the proto service files inside the builds folder if they are already not available only or you are facing any issue due to different environment.
   `python -m grpc_tools.protoc -I definitions/ --python_out=definitions/builds/ --grpc_python_out=definitions/builds/ definitions/service.proto`

## Running the Application

### Server

Run the gRPC server using `server.py`:
`python server.py`

### Client

Run the gRPC client using `client.py`:
`python client.py`

### Efficiency Comparison

The application also includes benchmarks to compare the efficiency of different web frameworks for building RESTful APIs. It includes:

- **Flask**: A lightweight web framework for building RESTful APIs in Python.
- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **MVC (Model-View-Controller) Architecture**: A traditional software design pattern for developing user interfaces.

Run the efficiency test using `test.py`:
`python test.py`

## Additional Notes

- Make sure to have Python and pip installed on your system.
- Ensure that the gRPC server is running before executing the client or efficiency test.
- You can get more details in my blog https://dhirajpatra.blogspot.com 

Thank you
