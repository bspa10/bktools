# encoding: utf-8

# Standard Library
from abc import ABC

# 3rd Party Library
# Current Folder
# Current Application
from bktools.exception import BKException

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class FrameworkException(BKException, ABC):
    pass
