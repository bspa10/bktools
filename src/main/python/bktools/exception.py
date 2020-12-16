# encoding: utf-8

# Standard Library
from abc import ABC
from typing import NoReturn

# 3rd Party Library
# Current Folder
# Current Application

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class BKException (RuntimeWarning, ABC):
    """
    Root Exception for the BK Ecosystem.

    The main goal here is to provide unique error code for every exception.
    """

    __slots__ = ('__code', '__message', )

    def __init__(self, code: str = None, message: str = None):
        super().__init__()

        self.__code = code
        self.__message = message

    @property
    def code(self) -> str:
        """
        Identification Code.
        """
        return self.__code

    @code.setter
    def code(self, value: str) -> NoReturn:
        if self.__code is not None:
            raise AttributeError('The exception [code] can\'t be redefined.')

        if value is None or len(value.strip()) == 0:
            raise AttributeError('The exception [code] must be a non-empty string.')

        self.__code = value

    @property
    def message(self) -> str:
        """
        Descriptive Message.
        """
        return self.__message

    @message.setter
    def message(self, value: str) -> NoReturn:
        if self.__message is not None:
            raise AttributeError('The exception [message] can\'t be redefined.')

        if value is None or len(value.strip()) == 0:
            raise AttributeError('The exception [message] must be a non-empty string.')

        self.__message = value

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.code}>'
