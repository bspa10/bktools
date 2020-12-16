# encoding: utf-8

# Standard Library
import inspect
import importlib
from typing import Any
from typing import Type
from typing import Tuple
from typing import List
from typing import Callable
from types import FunctionType

# 3rd Party Library
# Current Folder
# Current Application
from bktools.ext.python.exception import GenericsException

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def fqdn(instance: Any) -> str:
    """
    Retrieves the Fully Qualified Domain Name of the object's class.

    :param instance: Instance of a object
    :return: The Fully Qualified Domain Name
    """
    return f"{instance.__class__.__module__}.{instance.__class__.__name__}"


def get_attr(module: str, name: str) -> Any:
    return getattr(importlib.import_module(module), name)


def execute(module: str, function: str, *args, **kwargs) -> Any:
    target = get_attr(module, function)

    if inspect.isfunction(target):
        return target(*args, **kwargs)

    raise GenericsException('', f"Target [{module}.{function}] is not a function")


def get_class(klass: str) -> Any:
    """
    Retrieve a class type.

    Parameters:
        klass: The fully qualified class name
    """
    return get_attr(*klass.rsplit(".", 1))


def get_instance(klass: str, *args, **kwargs) -> Any:
    """
    Create an instance/object of the requested class.

    Its expected that the klass name to be fully qualified, that is, with the module name.

    Parameters:
        klass: The fully qualified class name
        args: The class __init__ parameters
        kwargs: The class __init__ parameters

    Returns:
        The created object
    """
    return get_class(klass)(*args, **kwargs)


def parameters(method: Callable) -> List[Tuple[str, Type]]:
    """
    Inspect the desired method extracting a list of parameters needed
    to execute it.

    Parameters:
        method: The type.Callable that will be inspected

    Returns:
        A list of Tuples with the parameter name and its annotation
    """
    output: List[Tuple[str, Type]] = list()
    if callable(method):
        spec: inspect.FullArgSpec = inspect.getfullargspec(method)

        if spec.args:
            for index in range(0, len(spec.args)):
                arg: str = spec.args[index]
                if arg == 'self' or arg == 'cls':
                    continue

                output.append((arg, spec.annotations[arg]))

    return output


def methods(source, interface=None) -> List[FunctionType]:
    output: List[FunctionType] = list()
    members = __list_public_functions(source)

    if interface:
        interface_members = __list_public_functions(interface)

        for im in interface_members:
            for sm in members:
                if sm.__name__ == im.__name__:
                    output.append(sm)

    else:
        output += members

    return output


def __list_public_functions(source) -> List[FunctionType]:
    output: List[FunctionType] = list()

    members: List = inspect.getmembers(source)
    for member in members:
        if not member[0].startswith('__') and isinstance(member[1], FunctionType):
            output.append(member[1])

    return output
