# encoding: utf-8

# Standard Library
from abc import ABC

# 3rd Party Library
# Current Folder
# Current Application
from bktools.framework.exception import FrameworkException

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class MoneyException(FrameworkException, ABC):
    pass


class CurrencyMismatchException(MoneyException):
    def __init__(self):
        super().__init__('00001', 'Trying to perform operation with different currencies.')
