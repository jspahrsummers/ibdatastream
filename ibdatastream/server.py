import asyncio
import concurrent.futures as futures
import logging
from typing import Optional

import grpc
import ib_insync as IB

from . import ibdatastream_pb2, ibdatastream_pb2_grpc, model


class Servicer(ibdatastream_pb2_grpc.IBDataStreamServicer):
    def __init__(self, ib: IB, eventLoop: asyncio.AbstractEventLoop):
        self._ib = ib
        self._loop = eventLoop
        super().__init__()

    def LookUp(self, request, context):
        async def _coroutine():
            contract = model.contract_from_lookup(request)

            logging.debug(f"Qualifying contract {contract}")
            await self._ib.qualifyContractsAsync(contract)
            logging.debug(f"Qualified contract: {contract}")

            return contract.conId

        logging.debug(f"LookUp({request})")
        conId = asyncio.run_coroutine_threadsafe(_coroutine(), self._loop).result()
        if not conId:
            raise RuntimeError(
                f"Could not qualify contract <{request}> (it may be ambiguous)"
            )

        return ibdatastream_pb2.Contract(contractID=conId)

    def Subscribe(self, request, context):
        pass


def start(
    port: int,
    ib: IB.IB,
    eventLoop: Optional[asyncio.AbstractEventLoop] = None,
    executor: Optional[futures.ThreadPoolExecutor] = None,
) -> grpc.Server:
    if eventLoop is None:
        eventLoop = asyncio.get_running_loop()

    if executor is None:
        executor = futures.ThreadPoolExecutor()

    s = grpc.server(executor)
    ibdatastream_pb2_grpc.add_IBDataStreamServicer_to_server(Servicer(ib, eventLoop), s)
    s.add_insecure_port(f"[::]:{port}")
    s.start()

    return s
