import asyncio
import concurrent.futures as futures
import signal
import unittest

import grpc

from ibdatastream import ibdatastream_pb2, ibdatastream_pb2_grpc, server
from ibdatastream.futures_bridge import future_to_aio_future

from tests import helpers


class TestServer(unittest.TestCase):
    port = 50051

    ev: asyncio.AbstractEventLoop
    server: grpc.Server
    stub: ibdatastream_pb2_grpc.IBDataStreamStub

    def setUp(self) -> None:
        # Install SIGINT handler. This is apparently necessary for the process to be interruptible with Ctrl-C on Windows:
        # https://bugs.python.org/issue23057
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        self.ev = asyncio.new_event_loop()
        self.server = server.start(self.port, helpers.StubIBClient(), self.ev)

        channel = grpc.insecure_channel(f"localhost:{self.port}")
        self.stub = ibdatastream_pb2_grpc.IBDataStreamStub(channel)

    def tearDown(self) -> None:
        self.ev.close()

    def test_look_up(self) -> None:
        f = self.stub.LookUp.future(ibdatastream_pb2.ContractLookup(symbol="SPY"))

        contract = self.ev.run_until_complete(future_to_aio_future(f, loop=self.ev))
        self.assertIsNotNone(contract)


if __name__ == "__main__":
    unittest.main()
