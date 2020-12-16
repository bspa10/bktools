# encoding: utf-8

# Standard Library
from typing import List
from typing import Tuple

# 3rd Party Library
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource

# Current Folder
from .constants import URL

# Current Application

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
SCOPES = [
    'https://www.googleapis.com/auth/drive',
]


class DriveApi(object):
    __slots__ = '__drive'

    def __init__(self, credential: Credentials):
        self.__drive: Resource = build('drive', 'v3', credentials=credential)

    def list_in_folder(self, folder: str, mime_type: str = None) -> List[Tuple]:
        folder_id = self.find_folder_by_name(folder)

        q = f"'{folder_id}' in parents"
        if mime_type:
            q = f"{q} and mimeType='{mime_type}'"

        token = None
        resource: Resource = self.__drive.files()
        results = resource.list(q=q, pageToken=token, fields='nextPageToken, files(id, name)', pageSize=1000).execute()
        files: List[Tuple] = list()
        for result in results.get('files', []):
            files.append((result['name'], result['id']))
        return files

    def find_folder_by_name(self, name: str) -> str:
        resource: Resource = self.__drive.files()

        results = resource.list(
            q=f"mimeType = 'application/vnd.google-apps.folder' and name = '{name}'",
            pageSize=10,
            fields="nextPageToken, files(id, name)"
        ).execute()

        return results.get('files', [])[0]['id']
