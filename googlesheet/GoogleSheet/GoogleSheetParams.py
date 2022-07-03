class GoogleSheetParams:
    def __init__(self, google_sheet_scope, token_path, credentials_path):
        self._google_sheet_scope = google_sheet_scope
        self._token_path = token_path
        self._credentials_path = credentials_path

    @property
    def google_sheet_scope(self):
        return self._google_sheet_scope

    @property
    def token_path(self):
        return self._token_path

    @property
    def credentials_path(self):
        return self._credentials_path
