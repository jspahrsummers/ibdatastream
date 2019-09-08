import concurrent.futures as futures
from typing import Optional

import grpc
import ib_insync as IB

from . import ibdatastream_pb2, ibdatastream_pb2_grpc


class Servicer(ibdatastream_pb2_grpc.IBDataStreamServicer):
    def __init__(self, ib: IB):
        self._ib = IB
        super().__init__()

    def LookUp(self, request, context):
        return ibdatastream_pb2.Contract(contractID=0)

    def Subscribe(self, request, context):
        pass


def start(
    port: int, ib: IB.IB, executor: Optional[futures.ThreadPoolExecutor] = None
) -> grpc.Server:
    if executor is None:
        executor = futures.ThreadPoolExecutor()

    s = grpc.server(executor)
    ibdatastream_pb2_grpc.add_IBDataStreamServicer_to_server(Servicer(ib), s)
    s.add_insecure_port(f"[::]:{port}")
    s.start()

    return s
