from google.protobuf.json_format import MessageToJson

from demo.proto.test_pb2 import HelloRequest
from grpc_help.client import client_channel
from demo.proto.test_pb2_grpc import GreeterStub

channel = client_channel("127.0.0.1:50051")
client = GreeterStub(channel)
response = client.simpleHello(HelloRequest(name="simple"))
rs = MessageToJson(response)
print(">>> 一对一 >>>>>", rs)

response = client.serverStreamHello(HelloRequest(name="streamServer"))
for r in response:
    rs = MessageToJson(r)
    print(">>> 服流 >>>>>", rs)


def generate_msg(name):
    for i in range(5):
        yield HelloRequest(name=f"{name}-{i}")

try:
    response = client.clientStreamHello(generate_msg("StreamRequest"))
    rs = MessageToJson(response)
    print(">>> 客流 >>>>>", rs)
except Exception as e:
    print("-----失败---", e)

try:
    response = client.biStreamHello(generate_msg("AllStream"))
    for r in response:
        rs = MessageToJson(r)
        print(">>> 双流 >>>>>", rs)
except Exception as e:
    print("-----失败---", e)
