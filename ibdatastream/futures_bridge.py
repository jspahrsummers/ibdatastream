import asyncio
import concurrent.futures
import grpc

from typing import Union


def grpc_future_to_concurrent_future(gf: grpc.Future) -> concurrent.futures.Future:
    cf: concurrent.futures.Future = concurrent.futures.Future()

    def gf_terminated(gf: grpc.Future) -> None:
        if gf.cancelled():
            cf.cancel()
            return

        try:
            result = gf.result(timeout=0)
            cf.set_result(result)
        except Exception as err:
            cf.set_exception(err)

    if cf.set_running_or_notify_cancel():
        gf.add_done_callback(gf_terminated)
    else:
        gf.cancel()

    return cf


AnyFuture = Union[concurrent.futures.Future, asyncio.Future, grpc.Future]


def future_to_aio_future(
    f: AnyFuture, loop: asyncio.AbstractEventLoop
) -> asyncio.Future:
    if isinstance(f, grpc.Future):
        return future_to_aio_future(grpc_future_to_concurrent_future(f), loop)
    elif isinstance(f, asyncio.Future):
        return f
    else:
        # HACK: This method definitely supports a `loop` argument, but mypy
        # doesn't think so.
        return asyncio.wrap_future(f, loop=loop)  # type: ignore
