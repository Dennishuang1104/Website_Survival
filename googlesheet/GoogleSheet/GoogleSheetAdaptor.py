from .GoogleSheetConnection import GoogleSheetConnection
from enum import Enum


class GoogleSheetScope:
    READONLY = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    READWRITE = 'https://www.googleapis.com/auth/spreadsheets'


class AdaptorMode(Enum):
    DEFAULT = -1
    QUERY_MODE = 0
    INSERT_MODE = 1
    CLEAR_MODE = 2
    BATCH_QUERY_MODE = 3


class GoogleSheetAdaptor:
    def __init__(self, GoogleSheet_Connection: GoogleSheetConnection):
        self.GoogleSheet_Connection = GoogleSheet_Connection.sheet
        self.GoogleSheetId = ''
        self.GoogleSheetRange = ''
        self.GoogleSheetMultiRange = []
        self.__fetch_data = []
        self.__map_mode = {AdaptorMode.QUERY_MODE: self.__get_data,
                           AdaptorMode.BATCH_QUERY_MODE: self.__batch_get_data,
                           AdaptorMode.INSERT_MODE: self.__insert_data,
                           AdaptorMode.CLEAR_MODE: self.__clear_data,
                           }
        self.mode = AdaptorMode.DEFAULT
        self.update_data = ''

    @property
    def READ_SCOPE(self):
        return GoogleSheetScope.READONLY

    @property
    def READWRITE(self):
        return GoogleSheetScope.READWRITE

    @property
    def QUERY_MODE(self):
        return AdaptorMode.QUERY_MODE

    @property
    def INSERT_MODE(self):
        return AdaptorMode.INSERT_MODE

    @property
    def CLEAR_MODE(self):
        return AdaptorMode.CLEAR_MODE

    @property
    def BATCH_QUERY_MODE(self):
        return AdaptorMode.BATCH_QUERY_MODE

    @property
    def fetch_data(self):
        return self.__fetch_data

    def __get_data(self):
        self.__fetch_data = []
        fetch_result = self.GoogleSheet_Connection.values().get(spreadsheetId=self.GoogleSheetId,
                                                                range=self.GoogleSheetRange).execute()
        self.__fetch_data = fetch_result.get('values', [])

    def __batch_get_data(self):
        self.__fetch_data = []
        fetch_result = self.GoogleSheet_Connection.values().batchGet(spreadsheetId=self.GoogleSheetId,
                                                                     ranges=self.GoogleSheetMultiRange).execute()
        fetch_data = fetch_result.get('valueRanges', [])
        for data in fetch_data:
            self.__fetch_data.append(data.get('values', []))

    def __insert_data(self):
        self._value_input_option = 'USER_ENTERED'
        self._value_range_body = {"values": [[self.update_data]]}
        self.GoogleSheet_Connection.values().update(spreadsheetId=self.GoogleSheetId,
                                                    range=self.GoogleSheetRange,
                                                    valueInputOption=self._value_input_option,
                                                    body=self._value_range_body).execute()

    def __clear_data(self):
        self.GoogleSheet_Connection.values().clear(spreadsheetId=self.GoogleSheetId,
                                                   range=self.GoogleSheetRange).execute()

    def exec(self):
        func = self.__map_mode[self.mode]
        func()
