# encoding: utf-8

# Standard Library
import logging
from os import path
from typing import List
from pathlib import Path

# 3rd Party Library
from typing import Optional
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.auth.transport.requests import AuthorizedSession

# Current Folder
from . import session
from .sheet import SpreadsheetApi

# Current Application

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
LOGGER = logging.getLogger(__name__)


class GoogleApi(object):
    __slots__ = ('__stored_credential', '__credential')

    def __init__(self):
        self.__stored_credential = f'{str(Path.home())}/.bktools/google/authorized_user.json'
        self.__credential: Optional[Credentials] = None

    def oauth(self, scopes: List[str]) -> bool:
        if path.exists(self.__stored_credential):
            self.__credential: Credentials = Credentials.from_authorized_user_file(self.__stored_credential)

        else:
            flow = InstalledAppFlow.from_client_secrets_file(self.__stored_credential, scopes)
            self.__credential: Credentials = flow.run_local_server(port=0)

            if self.__credential.valid:
                with open(self.__stored_credential, 'w') as f:
                    f.write(self.__credential.to_json('token'))

        if self.__credential.expired:
            self.__credential.refresh(Request())

        session.set(AuthorizedSession(self.__credential))
        return self.__credential.valid

    def spreadsheet(self) -> SpreadsheetApi:
        return SpreadsheetApi(self.__credential)
