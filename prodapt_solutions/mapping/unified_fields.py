
from typing import Any
from datetime import datetime
from dataclasses import dataclass
from config.bank_config import BankConfig
from helper.enum_definitions import AmountFormatEnum
from helper.enum_definitions import TransDirectionEnum

@dataclass
class UnifiedFields:

    date    : Any   = None
    fromId  : int   = None
    toId    : int   = None
    txd     : str   = None # transaction direction
    amount  : float = None

class UnifiedFieldsConvertor:

    def __init__(self, bankConfig: BankConfig):

        self.bankConfig: BankConfig = bankConfig

    def convert(self, data: dict) -> UnifiedFields:

        u = UnifiedFields()
        b = self.bankConfig

        # note negative cases are not yet handled

        u.date = data[b.DatetimeFieldName]
        u.date = datetime.strptime(u.date, b.DateExpr)

        if b.AmountFormat == AmountFormatEnum.Join:
            u.amount = float(data[b.AmountFieldName])
        else:
            u.amount = float(data[b.AmountIntegerFieldName] + 
                "." + data[b.AmountFractionFieldName])

        u.txd = TransDirectionEnum(data[b.TxdFieldName])

        u.fromId = data[b.FromFieldName]
        u.toId = data[b.ToFieldName]

        return u
    