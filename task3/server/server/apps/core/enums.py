from enum import Enum


class CurrencyEnum(Enum):
    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"
    RSD = "RSD"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)
