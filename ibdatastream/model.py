from . import ibdatastream_pb2
from decimal import Decimal

import ib_insync as IB

from typing import Any

_ContractLookup: Any = ibdatastream_pb2.ContractLookup

_security_type_mapping = {
    _ContractLookup.SecurityType.STOCK: "STK",
    _ContractLookup.SecurityType.OPTION: "OPT",
    _ContractLookup.SecurityType.FUTURE: "FUT",
    _ContractLookup.SecurityType.INDEX: "IND",
    _ContractLookup.SecurityType.FUTURES_OPTION: "FOP",
    _ContractLookup.SecurityType.CASH: "CASH",
    _ContractLookup.SecurityType.CFD: "CFD",
    _ContractLookup.SecurityType.COMBO: "BAG",
    _ContractLookup.SecurityType.WARRANT: "WAR",
    _ContractLookup.SecurityType.BOND: "BOND",
    _ContractLookup.SecurityType.COMMODITY: "CMDTY",
    _ContractLookup.SecurityType.NEWS: "NEWS",
    _ContractLookup.SecurityType.FUND: "FUND",
}

_right_mapping = {
    _ContractLookup.Right.UNSET: "",
    _ContractLookup.Right.PUT: "P",
    _ContractLookup.Right.CALL: "C",
}


def contract_from_lookup(lookup: Any) -> IB.Contract:
    """Converts a ContractLookup message into an ib_insync Contract object."""

    return IB.Contract(
        symbol=lookup.symbol,
        secType=_security_type_mapping[lookup.securityType],
        lastTradeDateOrContractMonth=lookup.lastTradeDateOrContractMonth,
        strike=Decimal(lookup.strike) if lookup.strike else 0.0,
        right=_right_mapping[lookup.right],
        multiplier=lookup.multiplier,
        exchange=lookup.exchange,
        currency=lookup.currency,
        localSymbol=lookup.localSymbol,
        primaryExchange=lookup.primaryExchange,
        tradingClass=lookup.tradingClass,
        includeExpired=lookup.includeExpired,
    )

