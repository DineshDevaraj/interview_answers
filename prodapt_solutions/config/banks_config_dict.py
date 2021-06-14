
from config.bank_config import BankConfig
from helper.enum_definitions import AmountFormatEnum

"""
It possible to read this configuration from JSON file
but for simplicity I have constructed Python object
"""
BanksConfigDict = {

    "bank1": BankConfig.default("bank1").update( 
        DateExpr = r"%b %d %Y", # Oct 1 2019
        DatetimeFieldName = "timestamp",
        TxdFieldName = "type"
    ),

    "bank2": BankConfig.default("bank2").update(
        DateExpr = r"%d-%m-%Y", # 03-10-2019
        AmountFieldName = "amounts"
    ),

    "bank3": BankConfig.default("bank3").update( 
        DateExpr = r"%d %b %Y", # 5 Oct 2019
        DatetimeFieldName = "date_readable",
        AmountFormat = AmountFormatEnum.Split,
        AmountIntegerFieldName = "euro",
        AmountFractionFieldName = "cents",
        TxdFieldName = "type",
    ),
}
