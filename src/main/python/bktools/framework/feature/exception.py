# encoding: utf-8

# Standard Library
# 3rd Party Library
# Current Folder
# Current Application
from bktools.framework.exception import FrameworkException

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class UnknownFeatureException(FrameworkException):
    """
    Exception thrown to indicate that a particular feature don't exists.
    """

    def __init__(self, name: str):
        super().__init__("0000", f"Feature [{name}] unknown")
