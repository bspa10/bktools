# encoding: utf-8

# Standard Library
import sys
from typing import Any
from typing import Set
from typing import NoReturn

# 3rd Party Library
# Current Folder
from .exception import InvalidParameterException
from .exception import MissingAttributeException
from .exception import AttributeSwappingException

# Current Application

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def swap(source: object, destination: object, attribute: str, nullable: bool = False) -> NoReturn:
    """
    Swap the value of a attribute between two objects.

    Parameters:
        source: The source object
        destination: The destination object
        attribute: The name of the desired attribute
        nullable: Flag indicating if the destination accept a NULL value
    """
    if source is None or destination is None or attribute is None:
        raise InvalidParameterException()

    attribute = attribute.strip()
    if len(attribute) <= 0:
        raise InvalidParameterException()

    if not hasattr(source, attribute) or not hasattr(destination, attribute):
        raise MissingAttributeException(attribute)

    if getattr(source, attribute) == getattr(destination, attribute):
        return

    value = getattr(source, attribute)
    if value is not None:
        setattr(destination, attribute, value)

    else:
        if nullable:
            setattr(destination, attribute, value)

        else:
            raise AttributeSwappingException(attribute)


def sizeof(obj: Any, seen: Set[Any] = None) -> int:
    """
    Recursively finds size of objects.

    Parameters:
        obj: The object that will be evaluated
        seen: Already visited objects

    Returns:
        The bytes of the object
    """
    size = sys.getsizeof(obj)

    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([sizeof(v, seen) for v in obj.values()])
        size += sum([sizeof(k, seen) for k in obj.keys()])

    elif hasattr(obj, '__dict__'):
        size += sizeof(obj.__dict__, seen)

    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([sizeof(i, seen) for i in obj])

    return size
