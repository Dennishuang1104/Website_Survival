import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
from . import GoogleSheetParams


class GoogleSheetConnection:
    def __init__(self, Params: GoogleSheetParams):
        self.GoogleSheetParams = Params
        self.__sheet = None
        self.create_a_new_connection()

    def create_a_new_connection(self):
        credentials = None
        if os.path.exists(self.GoogleSheetParams.token_path):
            with open(self.GoogleSheetParams.token_path, 'rb') as token:
                credentials = pickle.load(token)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.GoogleSheetParams.credentials_path, self.GoogleSheetParams.google_sheet_scope)
                credentials = flow.run_local_server(port=0)
            with open(self.GoogleSheetParams.token_path, 'wb') as token:
                pickle.dump(credentials, token)
        service = build('sheets', 'v4', credentials=credentials, cache_discovery=False)
        self.__sheet = service.spreadsheets()

    @property
    def sheet(self):
        return self.__sheet
