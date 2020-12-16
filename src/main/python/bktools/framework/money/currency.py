# encoding: utf-8

# Standard Library
from os import path
from threading import Lock
from typing import Set
from typing import Optional
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element

# 3rd Party Library
# Current Folder
# Current Application

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class Currency(object):
    """
    ISO 4217 currency.
    """
    __slots__ = ('__code', '__name', '__number', '__precision')

    def __init__(self, code: str, name: str, number: int, precision: int):
        self.__code = code
        self.__name = name
        self.__number = number
        self.__precision = precision

    @property
    def code(self) -> str:
        """
        The currency code which consist of 3 uppercase characters.

        e.g: USD, BRL
        """
        return self.__code

    @property
    def name(self) -> str:
        """
        Currency Name. i.e. US Dollar, Brazilian Real
        """
        return self.__name

    @property
    def number(self) -> int:
        """
        The currency number.

        e.g:
        840 -> US Dollar
        986 -> Brazilian Real
        """
        return self.__number

    @property
    def precision(self) -> int:
        """
        The treatment of minor currency unit, in exponent where base is 10.
        For example, a U.S. dollar is 100 cents, witch is 2.
        """
        return self.__precision

    #: -=-=-=-=-=-=-=-=-=-=-=
    #: Comparation Functions
    #: -=-=-=-=-=-=-=-=-=-=-=

    def __eq__(self, other):
        if not isinstance(other, Currency):
            return False

        return self.number == other.number

    #: -=-=-=-=-=-=-=-=-=-=-=
    #: Utility Functions
    #: -=-=-=-=-=-=-=-=-=-=-=

    def __hash__(self):
        return hash(self.number)

    def __repr__(self):
        return f'{self.__class__.__name__} {self.code}'


class Currencies(object):
    """
    Factory of ISO 4217 - Currency Code.
    """

    __slots__ = '_'
    __guard = Lock()
    __entries: Set[Currency] = set()
    __BASE_DIR = path.abspath(path.dirname(__file__))

    def __init__(self):
        with self.__guard:
            if self.__entries:
                return

            #: http://www.currency-iso.org/dam/downloads/lists/list_one.xml
            file = path.abspath(f'{self.__BASE_DIR}/iso4217.xml')
            raw: Element = ET.parse(file)

            for node in raw.findall('CcyTbl/CcyNtry'):
                country = self.__get_value(node, 'CtryNm')
                if country and country.startswith('ZZ'):
                    # Ignore none-real countries
                    continue

                code = self.__get_value(node, 'Ccy')
                name = self.__get_value(node, 'CcyNm')
                number = self.__get_value(node, 'CcyNbr')
                unit = self.__get_value(node, 'CcyMnrUnts')

                if code and name and number:
                    try:
                        currency = Currency(code, name, int(number), int(unit))
                    except (TypeError, ValueError):
                        currency = Currency(code, name, int(number), 0)

                    self.__entries.add(currency)

    @staticmethod
    def __get_value(node: Element, key: str) -> Optional[str]:
        element = node.find(key)
        if element is not None:
            return element.text.strip()

        return None

    @classmethod
    def code(cls, code: str) -> Optional[Currency]:
        """
        Retrieve the Currency object by its code.
        e.g. BRL, USD

        Parameters:
            code: The currency code. e.g. BRL

        Returns:
            the Currency object
        """
        code = code.upper()

        for entry in cls().__entries:
            if entry.code == code:
                return entry

        return None

    @classmethod
    def number(cls, number: int) -> Optional[Currency]:
        """
        Retrieve the Currency object by its number.
        e.g. 986 (BRL), 840 (USD)

        Parameters:
            number: The currency number. e.g. 840 (USD)

        Returns:
            the Currency object
        """
        for entry in cls().__entries:
            if entry.number == number:
                return entry

        return None
