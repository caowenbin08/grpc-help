from grpc_help.rules import RpcServicerBlueprint
from . import async_test
rpc_blueprint = RpcServicerBlueprint()
rpc_blueprint.add_service_blueprint(async_test.blueprint)
