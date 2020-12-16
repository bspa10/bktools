# encoding: utf-8

# Standard Library
import json
from typing import Any
from typing import Dict
from typing import List
from typing import Union
from typing import Optional
from typing import NoReturn

# 3rd Party Library
from requests import Response

# Current Folder
from .exception import ColumnException
from .exception import SpreadsheetException

# Current Application
from bktools.framework.google import session

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class Column(object):
    __slots__ = ('__index', '__value', )

    def __init__(self, index: Union[int, str]):
        self.__index = index

    @property
    def index(self) -> Union[int, str]:
        return self.__index

    @property
    def empty(self) -> bool:
        return self.__value is None

    @property
    def value(self) -> Optional[Any]:
        return self.__value

    @property
    def string(self) -> Optional[Any]:
        return self.__value

    @property
    def integer(self) -> Optional[Any]:
        return int(self.__value) if self.__value else None

    @property
    def decimal(self) -> Optional[Any]:
        return float(self.__value) if self.__value else None


class Row(object):
    __slots__ = ('__index', '__columns', )

    def __init__(self, index: int):
        self.__index = index
        self.__columns: List[Column] = list()

    @property
    def index(self) -> int:
        return self.__index

    def add_column(self, column: Column) -> NoReturn:
        if [r for r in self.__columns if r.__index == column.__index]:
            raise ColumnException('', '')

        self.__columns.append(column)

    def columns(self) -> List[Column]:
        return self.__columns


class Worksheet(object):
    __slots__ = ('__spreadsheet', '__identity', '__index', '__title', '__rows')

    def __init__(self, spreadsheet: str, properties: Dict):
        self.__spreadsheet: str = spreadsheet
        self.__identity: str = properties['sheetId']
        self.__index: int = int(properties['index'])
        self.__title: str = properties['title']
        self.__rows: List[Row] = list()

    @property
    def identity(self) -> int:
        return int(self.__identity)

    @property
    def index(self) -> int:
        return int(self.__index)

    @property
    def title(self) -> str:
        return self.__title

    @property
    def rows(self) -> List[Row]:
        return self.__rows

    def load(self) -> NoReturn:

        result: Response = session.execute('sheet', 'get', 'general', self.__spreadsheet, params={
            'ranges': self.title,
            'includeGridData': True
        })

        print(json.loads(result.text))

    def __repr__(self):
        return f"<Worksheet [{self.index}][{self.title}]>"


class Spreadsheet(object):
    __slots__ = ('__sheet', '__identity', '__title', '__url', '__worksheets')

    def __init__(self, identity: str, title: str):
        self.__identity = identity
        self.__title = title
        self.__worksheets: List[Worksheet] = list()

        result: Response = session.execute('sheet', 'get', 'general', identity)
        metadata: Dict = json.loads(result.text)

        self.__url = metadata['spreadsheetUrl']
        for sheet in metadata['sheets']:
            self.__worksheets.append(Worksheet(self.__identity, sheet['properties']))

    @property
    def identity(self) -> str:
        return self.__identity

    @property
    def title(self) -> str:
        return self.__title

    def create(self, title: str, rows: int, cols: int, index: int = None) -> Worksheet:
        body = {
            'requests': [
                {
                    'addSheet': {
                        'properties': {
                            'title': title,
                            'sheetType': 'GRID',
                            'gridProperties': {
                                'rowCount': rows,
                                'columnCount': cols
                            }
                        }
                    }
                }
            ]
        }

        if index is not None:
            body["requests"][0]["addSheet"]["properties"]["index"] = index

        result: Response = session.execute('sheet', 'post', 'batch_update', self.__identity, body)
        if result.status_code == 400:
            payload = json.loads(result.text)['error']
            raise SpreadsheetException(payload['code'], payload['message'])

        worksheet = Worksheet(self.identity, json.loads(result.text)['replies'][0]['addSheet']['properties'])
        self.__worksheets.append(worksheet)

        return worksheet

    def delete(self, worksheet: Worksheet) -> NoReturn:
        body = {
            'requests': [
                {
                    'deleteSheet': {
                        'sheetId': worksheet.identity
                    }
                }
            ]
        }

        session.execute('sheet', 'post', 'batch_update', self.__identity, body)
        self.__worksheets.remove(worksheet)

    def worksheets(self) -> List[Worksheet]:
        return self.__worksheets

    def __repr__(self):
        return f"<Spreadsheet [{self.__title}][{self.__identity}]>"
