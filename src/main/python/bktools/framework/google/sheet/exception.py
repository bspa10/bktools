# encoding: utf-8

# Standard Library
from abc import ABC

# 3rd Party Library
# Current Folder
# Current Application
from bktools.framework.google.exception import GoogleApiException

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class GoogleSpreadsheetException(GoogleApiException, ABC):
    pass


class SpreadsheetException(GoogleSpreadsheetException):
    pass


class WorksheetException(GoogleSpreadsheetException):
    pass


class ColumnException(GoogleSpreadsheetException):
    pass
