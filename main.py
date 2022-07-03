from Repository.Adaptor.GoogleSht.SheetAdaptor import SheetAdaptor
from Repository.Adaptor.GCP.GCSImgAdaptor import GCSImgAdaptor
from WebDriver import WebDriver
import time , datetime
import requests
import Environment as envi
import pandas as pd
import os, csv

def main():
    # Google sheet 取得網址Link
    sheet = SheetAdaptor()
    source_sheet = sheet.get_twitter_data()
    my_headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 "
                                    "(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    webdriver = WebDriver()
    # 上傳到GCS
    ggl_storage = GCSImgAdaptor()
    date_time = datetime.datetime.today().strftime('%Y%m%d')

    link = []
    promotion_id = []
    website_status = []
    for c in source_sheet:
        link.append(c[0])
        promotion_id.append(c[1])
        try:
            response_status = str(requests.get(c[0], headers=my_headers))
            if response_status == '<Response [200]>':
                try:
                    webdriver.do_init()
                    webdriver.driver.maximize_window()
                    webdriver.driver.get(c[0])
                    img_name = f'{c[1]}.png'
                    gcs_img_name = date_time + '_' + img_name
                    time.sleep(5)
                    webdriver.driver.get_screenshot_as_file(f'{envi.img_folder}/{img_name}')
                    ggl_storage.upload_img(img_name, gcs_img_name)
                    os.remove(envi.img_folder + img_name)
                    website_status.append(0)

                except Exception as e:
                    website_status.append(1)
                    print(f'{c[1]} 錯誤')
                    # print(f'Error : {e}')

            else:
                website_status.append(1)
                print(f'{c[1]} 錯誤')
                # print(f'{c[1]} response status error')

        except Exception as e:
            website_status.append(1)
            print(f'{c[1]} 錯誤')
            # print('link error!')

    # 將結果用csv 儲存
    if not os.path.exists(envi.result_csv):
        with open(envi.result_csv, 'w', newline='') as csv_file:
            result = csv.writer(csv_file)
            result.writerow(['連結', '代號'])
    result = pd.read_csv(envi.result_csv)
    result['連結'] = pd.Series(link)
    result['代號'] = pd.Series(promotion_id)
    result[f'{date_time}_result'] = pd.Series(website_status)
    result.to_csv(envi.result_csv)
    webdriver.do_bot_close()

if __name__ == '__main__':
    main()
