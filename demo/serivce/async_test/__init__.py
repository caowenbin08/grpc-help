from grpc_help.rules import ServiceBlueprint
from demo.proto.test_pb2_grpc import add_GreeterServicer_to_server, GreeterServicer
blueprint = ServiceBlueprint(servicer=add_GreeterServicer_to_server, service=GreeterServicer)
from . import view
blueprint.add_method("serverStreamHello", view.ServerStreamHello)
blueprint.add_method("clientStreamHello", "demo.serivce.async_test.view.ClientStreamHello")
