import concurrent.futures as futures
import unittest

import grpc

from ibdatastream import ibdatastream_pb2, ibdatastream_pb2_grpc, server


class TestServer(unittest.TestCase):
    port = 50051
    stub: ibdatastream_pb2_grpc.IBDataStreamStub

    def setUp(self) -> None:
        s = grpc.server(futures.ThreadPoolExecutor())
        ibdatastream_pb2_grpc.add_IBDataStreamServicer_to_server(server.Servicer(), s)
        s.add_insecure_port(f"[::]:{self.port}")
        s.start()

        channel = grpc.insecure_channel(f"localhost:{self.port}")
        self.stub = ibdatastream_pb2_grpc.IBDataStreamStub(channel)

    def test_look_up(self) -> None:
        contract = self.stub.LookUp(ibdatastream_pb2.ContractLookup(symbol="SPY"))
        self.assertIsNotNone(contract)


if __name__ == "__main__":
    unittest.main()
