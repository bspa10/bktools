# encoding: utf-8

# Standard Library
from typing import Optional

# 3rd Party Library
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource
from google.oauth2.credentials import Credentials

# Current Folder
from .logger import LOGGER
from .model import Spreadsheet

# Current Application
from bktools.framework.google.drive import DriveApi

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets',
]


class SpreadsheetApi(object):
    __slots__ = ('__session', '__sheet', '__drive')

    def __init__(self, credential: Credentials):
        self.__sheet: Resource = build('sheets', 'v4', credentials=credential).spreadsheets()
        self.__drive: DriveApi = DriveApi(credential)

    def open(self, folder: str, name_or_id: str) -> Optional[Spreadsheet]:
        LOGGER.info(f'Abrindo planilha [{folder}][{name_or_id}]')

        for file in self.__drive.list_in_folder(folder, 'application/vnd.google-apps.spreadsheet'):
            if file[0] == name_or_id or file[1] == name_or_id:
                return Spreadsheet(file[1], file[0])

        return None
