from googlesheet.GoogleSheet.GoogleSheetParams import GoogleSheetParams
from googlesheet.GoogleSheet.GoogleSheetConnection import GoogleSheetConnection
from googlesheet.GoogleSheet.GoogleSheetAdaptor import GoogleSheetAdaptor, GoogleSheetScope
import os


class SheetAdaptor(GoogleSheetAdaptor):
    def __init__(self):
        """
        need input : token_path, credentials_path, googlesheetid
        """
        ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
        super(SheetAdaptor, self).__init__(GoogleSheetConnection(
            GoogleSheetParams(google_sheet_scope=[GoogleSheetScope.READWRITE],
                              token_path=f'cred/token.pickle',
                              credentials_path=f'cred/credentials.json')))
        self.GoogleSheetId = 'yourid'

    def get_twitter_data(self):
        """
        提供 GoogleSheetRange 以抓取一個 Range 下的值 (只能輸入一個範圍)
        :return:
        """
        self.mode = self.QUERY_MODE
        self.GoogleSheetRange = 'row:column'
        self.exec()
        return self.fetch_data

    def batchget_twitter_data(self):
        """
        提供 GoogleSheetRange 以抓取多個 Ranges 下的值（可輸入多個範圍)
        :return:
        """
        self.mode = self.BATCH_QUERY_MODE
        self.GoogleSheetMultiRange.append('row:column')
        self.GoogleSheetMultiRange.append('row:column')
        self.exec()
        return self.fetch_data

    def insert_twitter_data(self):
        """
        提供 GoogleSheetRange 以更新該欄位的值 (只能輸入單一欄位）
        :return:
        """
        self.mode = self.INSERT_MODE
        self.GoogleSheetRange = 'row:column'
        self.update_data = 'xxxx'
        self.exec()

    def clear_twitter_data(self):
        """
        提供 GoogleSheetRange 以清除該欄位的值(只能輸入一個範圍)
        :return:
        """
        self.mode = self.CLEAR_MODE
        self.GoogleSheetRange = 'row:column'
        self.exec()


def main():
    try:
        sheet = SheetAdaptor()
        # sheet.insert_twitter_data()
        fetch_data = sheet.get_twitter_data()
        # fetch_data = sheet.batchget_twitter_data()
        print(f'{fetch_data}')
        # sheet.clear_twitter_data()
    except Exception as e:
        print(f'Error : {e}')


if __name__ == '__main__':
    main()
