# encoding: utf-8

# Standard Library
from typing import Any
from typing import Dict
from typing import NoReturn

# 3rd Party Library
from requests import Response
from google.auth.transport.requests import AuthorizedSession

# Current Folder
from .sheet.constants import URL as S_URL
from .drive.constants import URL as D_URL

# Current Application

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
__buffer: Dict[str, Any] = dict()


def set(session: AuthorizedSession) -> NoReturn:
    __buffer['session'] = session


def execute(api: str, verb: str, action: str, target: str, body: Any = None, params: Dict = None) -> Response:
    """
    Execute the Google API Call

    Parameters:
        api: The API name ('sheet' or 'drive')
        verb: The HTTP Verb
        action: The action that will be executed
        target: The resource ID of the API Call
        body: HTTP Payload
        params: HTTP URL Parameters

    Returns:
        The response object of the call
    """
    if 'sheet' in api:
        return __do_execute_sheet(verb, action, target, body, params)

    if 'drive' in api:
        return __do_execute_drive(verb, action, target, body, params)


def __do_execute_sheet(verb: str, action: str, target: str, body: Any = None, params: Dict = None) -> Response:
    return __do_execute(verb, S_URL[action] % target, body, params)


def __do_execute_drive(verb: str, action: str, target: str, body: Any = None, params: Dict = None) -> Response:
    return __do_execute(verb, D_URL[action] % target, body, params)


def __do_execute(verb: str, url: str, body: Any, params: Dict) -> Response:
    session = __buffer['session']

    if body:
        if params:
            return getattr(session, verb)(url, params=params, json=body)
        return getattr(session, verb)(url, params=params, json=body)

    if params:
        return getattr(session, verb)(url, params=params)

    return getattr(session, verb)(url)
