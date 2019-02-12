from google.protobuf.json_format import MessageToJson

from demo.proto.test_pb2 import HelloRequest
from grpc_help.client import client_channel
from demo.proto.test_pb2_grpc import GreeterStub

channel = client_channel("127.0.0.1:50051")
req = HelloRequest(name="simple")
client = GreeterStub(channel)
response = client.simpleHello(req)
rs = MessageToJson(response)
print(">>>>>>>>", rs)