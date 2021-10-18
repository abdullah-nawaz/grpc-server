from concurrent import futures

import grpc
from grpc._cython.cygrpc import CompressionAlgorithm
from grpc._cython.cygrpc import CompressionLevel

from server.rpc.rpc_server.calls import GCPResponseCalls
from server.rpc.rpc_server.config import GRPCConfigs
from server.rpc.rpc_server.proto_files import rpc_responses_grpc_def_pb2_grpc


def run():
    app = grpc.server(
        futures.ThreadPoolExecutor(max_workers=GRPCConfigs.WORKERS),
        options=[
            ("grpc.max_send_message_length", GRPCConfigs.MAX_MESSAGE_SIZE),
            ("grpc.max_receive_message_length", GRPCConfigs.MAX_MESSAGE_SIZE),
            ("grpc.default_compression_algorithm", CompressionAlgorithm.gzip),
            ("grpc.default_compression_level", CompressionLevel.high),
        ],
    )

    rpc_responses_grpc_def_pb2_grpc.add_ResponseCallsServicer_to_server(
        GCPResponseCalls(), app
    )
    app.add_insecure_port("0.0.0.0:{}".format(GRPCConfigs.PORT))

    app.start()
    app.wait_for_termination()


if __name__ == "__main__":
    run()
