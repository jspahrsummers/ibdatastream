import asyncio

from ibdatastream.ib import Contract, IBClient


class StubIBClient(IBClient):
    async def qualify_contract_inplace(self, contract: Contract) -> None:
        return
