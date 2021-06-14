
from typing import Any
from dataclasses import dataclass

from helper.enum_definitions import InputMethodEnum
from helper.enum_definitions import InputFormatEnum
from helper.enum_definitions import AmountFormatEnum
from helper.enum_definitions import DatetimeFromatEnum

from helper.exception_definitions import InvalidField

@dataclass
class BankConfig:

    BankName: str

    InputMethod: InputMethodEnum
    InputFormat: InputFormatEnum

    InputReaderConfig: Any

    """
        InputReaderConfig value should follow the below logic 

        if InputMethod == InputMethodEnum.DB:
            InputReaderConfig = DBReaderConfig()
        elif InputMethod == InputMethodEnum.REST:
            InputReaderConfig = RestReaderConfig()
        else: # InputMethod == InputMethodEnum.FILE:
            InputReaderConfig = FileReaderConfig()
    """

    DatetimeFormat: DatetimeFromatEnum

    DateFieldName: str
    TimeFieldName: str

    DatetimeFieldName: Any

    # Refere strptime() to know the format directives
    DateExpr: str

    """
    DatetimeFieldName value should follow the below logic

    if datetime_format == datetime_format_enum.split:
    datetime_field_name: tuple = (date_field_name, time_field_name)
    else:
    datetime_field_name: string = timestamp, date_readable, date, etc...
    """

    AmountFormat: AmountFormatEnum

    AmountIntegerFieldName: str
    AmountFractionFieldName: str

    AmountFieldName: Any

    """
    AmountFieldName value should follow the below logic

    if AmountFormat == AmountFormat.Split:
    amount_field_name: tuple = (amount_integer_name, amount_fraction_name)
    else:
    amount_field_name: string = amount, amounts, etc...
    """

    TxdFieldName: str # Txd - Transaction Direction

    FromFieldName: str
    ToFieldName: str

    @staticmethod
    def default(bankName: str):

        bankConfig = BankConfig(

            BankName = bankName,

            InputMethod = InputMethodEnum.File,
            InputFormat = InputFormatEnum.CSV,
            InputReaderConfig = None,

            DatetimeFormat = DatetimeFromatEnum.Join,
            DateFieldName = None,
            TimeFieldName = None,
            DatetimeFieldName = "date",
            DateExpr = r"%d/%b/%Y",

            AmountFormat = AmountFormatEnum.Join,
            AmountIntegerFieldName = None,
            AmountFractionFieldName = None,
            AmountFieldName = "amount",

            TxdFieldName = "transaction",

            FromFieldName = "from",
            ToFieldName = "to"

        )

        return bankConfig

    def update(self, **kwargs):

        for k, v in kwargs.items():
            if not hasattr(self, k):
                raise InvalidField(k)
            setattr(self, k, v)
        return self
