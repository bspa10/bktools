# encoding: utf-8

# Standard Library
import sys
from importlib import util

# 3rd Party Library
# Current Folder
# Current Application

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def is_imported(name: str) -> bool:
    """
    Utility function to indicate if a module has been imported.

    Parameter:
        name: The module name

    Returns:
        True if the module has been imported, false otherwise.
    """
    return name in sys.modules


def exists(name: str) -> bool:
    """
    Check if a module exists in VENV.

    Parameter:
        name: The name of the module

    Returns:
          True if the module exists in venv, False otherwise.
    """
    return util.find_spec(name) is not None
