"""
blob: the filename in google cloud storage (can be a folder with name ex: imgs/xxx.jpg)
file: local file (can be a path with filename)
"""
from googlecloudstorage.CloudStorage.Adaptor import CloudStorageAdaptor
import Environment as envi


class GCSImgAdaptor(CloudStorageAdaptor):
    def __init__(self):
        super(GCSImgAdaptor, self).__init__('goa_vietnam_website_screenshot', envi.img_upload_cred_path)
        self.img_folder = envi.img_folder

    def upload_img(self, img_name, gcs_img_name):
        self.mode = self.UPLOAD_MODE
        self.blob = gcs_img_name
        self.file = self.img_folder + img_name
        self.exec()

    def download_img(self, img_name):
        self.mode = self.DOWNLOAD_MODE
        self.blob = img_name
        self.file = self.img_folder + img_name
        self.exec()


