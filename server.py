from grpc_help import grpcserver


def run():
    grpcserver.start(
        address_port="[::]:50051",
        ssl=False,
        workers=2,
        rpc_root_ruleconf="demo.serivce.rpcs"
    )

run()
