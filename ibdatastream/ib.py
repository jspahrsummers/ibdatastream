from abc import ABC, abstractmethod
import asyncio
import ib_insync
from ib_insync import Contract


class IBClient(ABC):
    @abstractmethod
    async def qualify_contract_inplace(self, contract: Contract) -> None:
        pass


class IBInSyncClient(IBClient):
    def __init__(self, ib: ib_insync.IB):
        self._ib = ib
        super().__init__()

    @property
    def ib(self) -> ib_insync.IB:
        return self._ib

    async def qualify_contract_inplace(self, contract: Contract) -> None:
        await self._ib.qualifyContractsAsync(contract)
