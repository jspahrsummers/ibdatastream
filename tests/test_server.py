import unittest

import grpc  # type: ignore
import concurrent.futures as futures
from ibdatastream import ibdatastream_pb2_grpc
from ibdatastream import server


class TestServer(unittest.TestCase):
    def test_start_server(self) -> None:
        s = grpc.server(futures.ThreadPoolExecutor())
        ibdatastream_pb2_grpc.add_IBDataStreamServicer_to_server(server.Servicer(), s)
        s.add_insecure_port("[::]:50051")
        s.start()


if __name__ == "__main__":
    unittest.main()
