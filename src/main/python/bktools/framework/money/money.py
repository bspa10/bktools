# encoding: utf-8

# Standard Library
from typing import Union
from typing import NoReturn

# 3rd Party Library
# Current Folder
# Current Application
from bktools.framework.money.currency import Currency
from bktools.framework.money.exception import CurrencyMismatchException

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class Money(object):
    __slots__ = ('__currency', '__amount', )

    def __init__(self, currency: Currency, amount: Union[str, float, int]):
        self.__currency = currency
        self.__amount = float(amount)

    @property
    def currency(self) -> Currency:
        return self.__currency

    @property
    def value(self) -> float:
        return float(self.__amount)

    #: -=-=-=-=-=-=-=-=-=-=-=
    #: Arithmetic Functions
    #: -=-=-=-=-=-=-=-=-=-=-=

    def __add__(self, other):
        self.__check_parameter(other)
        value = self.__amount + other.__amount
        rounded = self.__round(value)

        return self.__class__(self.currency, rounded)

    def __sub__(self, other):
        self.__check_parameter(other)
        value = self.__amount - other.__amount
        rounded = self.__round(value)

        return self.__class__(self.currency, rounded)

    def __mul__(self, other):
        self.__check_parameter(other)
        value = self.__amount * other.__amount
        rounded = self.__round(value)

        return self.__class__(self.currency, rounded)

    def __abs__(self):
        return self.__class__(self.currency, abs(self.value))

    def __neg__(self):
        return self.__class__(self.currency, str(-self.value))

    def __pos__(self):
        return self.__class__(self.currency, abs(self.value))

    #: -=-=-=-=-=-=-=-=-=-=-=
    #: Comparation Functions
    #: -=-=-=-=-=-=-=-=-=-=-=

    def __eq__(self, other) -> bool:
        self.__check_parameter(other)
        return self.value == other.value

    def __ne__(self, other) -> bool:
        self.__check_parameter(other)
        return not self == other

    def __lt__(self, other):
        self.__check_parameter(other)
        return self.value < other.value

    def __le__(self, other):
        self.__check_parameter(other)
        return self.value <= other.value

    def __gt__(self, other):
        self.__check_parameter(other)
        return self.value > other.value

    def __ge__(self, other):
        self.__check_parameter(other)
        return self.value >= other.value

    #: -=-=-=-=-=-=-=-=-=-=-=
    #: Utility Functions
    #: -=-=-=-=-=-=-=-=-=-=-=

    def __bool__(self):
        return self.value == 0

    def __hash__(self):
        return hash((self.__currency, self.__amount))

    #: -=-=-=-=-=-=-=-=-=-=-=
    #: Representation Functions
    #: -=-=-=-=-=-=-=-=-=-=-=

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.currency.code} {self.value}>'

    #: -=-=-=-=-=-=-=-=-=-=-=
    #: Internal Utility
    #: -=-=-=-=-=-=-=-=-=-=-=

    def __check_parameter(self, other) -> NoReturn:
        if not isinstance(other, Money):
            raise TypeError()

        if self.currency != other.currency:
            raise CurrencyMismatchException()

    def __round(self, amount):
        return round(amount, self.currency.precision)
