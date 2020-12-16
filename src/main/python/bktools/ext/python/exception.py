# encoding: utf-8

# Standard Library
from abc import ABC

# 3rd Party Library
# Current Folder
# Current Application
from bktools.ext.exception import ExtensionsException

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class PythonExtensionException(ExtensionsException, ABC):
    pass


class InvalidParameterException (PythonExtensionException):
    def __init__(self):
        super().__init__('00008', 'All parameters must be supplied')


class MissingAttributeException (PythonExtensionException):
    def __init__(self, attribute: str):
        super().__init__('00017', f'[source] or [destiny] do not have the attribute [{attribute}]')


class AttributeSwappingException (PythonExtensionException):
    def __init__(self, value: str):
        super().__init__('00018', f'Unable to swap [{value}] attribute')


class ApiViolationException(PythonExtensionException):
    pass


class GenericsException(PythonExtensionException):
    pass
