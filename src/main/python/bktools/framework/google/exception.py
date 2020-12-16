# encoding: utf-8

# Standard Library
from abc import ABC
# 3rd Party Library
# Current Folder
# Current Application
from bktools.framework.exception import FrameworkException

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class GoogleApiException(FrameworkException, ABC):
    pass
