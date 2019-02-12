from demo.proto.test_pb2 import HelloReply
from demo.serivce.async_test import blueprint
from grpc_help.views import AsyncGenericRpcView, AsyncStreamRpcView


@blueprint.method("simpleHello")
class SimpleHelloView(AsyncGenericRpcView):
    proto_response_class = HelloReply

    async def view_handle(self, *args, **kwargs):
        name = self.data["name"]
        return dict(message=f"hello {name}")


class ServerStreamHello(AsyncStreamRpcView):
    proto_response_class = HelloReply

    async def view_handle(self, *args, **kwargs):
        name = self.data["name"]
        for i in range(3):
            # await asyncio.sleep(2)
            yield dict(message=f"hello {name}-{i}")


class ClientStreamHello(AsyncGenericRpcView):
    proto_response_class = HelloReply

    async def view_handle(self, *args, **kwargs):
        names = []
        for d in self.data:
            name = d["name"]
            names.append(name)
        return dict(message=f"hello {names}")


@blueprint.method("biStreamHello")
class BiStreamHello(AsyncStreamRpcView):
    proto_response_class = HelloReply

    async def view_handle(self, *args, **kwargs):
        for d in self.data:
            name = d["name"]
            yield dict(message=f"hello 1 {name}")

