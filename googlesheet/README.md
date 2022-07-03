# GoogleSheet

GoogleSheet Adaptor

使用前須人工執行

1. 使用前須先登入 google , 並前往 https://developers.google.com/sheets/api/quickstart/python 下載 CLIENT CONFIGURATION(credentials.json)。
2. 將 credentials.json檔案放置專案下，並將路徑填入 credentials_tath 中。
3. 執行GoogleSheetAdptor時程式會自動前往拿token的網站，須再次登入google帳號,以及須確認提供的googlesheet id的是否有提供給該帳號讀取權限，
   成功會出現 The authentication flow has completed. You may close this window.，並產生 token.pickle。
4. 將 token.pickle 的檔案位置填入 token_path 中。

詳細使用方式請參考 GoogleSheetExampleAdaptor.py