from . import ibdatastream_pb2_grpc

import grpc


def new_test_client(
    port: int, host: str = "localhost"
) -> ibdatastream_pb2_grpc.IBDataStreamStub:
    channel = grpc.insecure_channel(f"{host}:{port}")
    return ibdatastream_pb2_grpc.IBDataStreamStub(channel)
