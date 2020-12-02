import io
import os
from urllib.request import urlopen
from zipfile import ZipFile
from os.path import join as join_paths


class COCOAnnotationsDownloader:
    _annotations_archive_url = "http://images.cocodataset.org/annotations/annotations_trainval{}.zip"

    def __init__(self, dataset_path, annotations_year):
        self.__dataset_path = dataset_path
        self.__annotations_folder_path = join_paths(self.__dataset_path, "annotations")
        self.__annotations_year = annotations_year

    def _annotations_exist(self):
        return os.listdir(self.__annotations_folder_path)

    def download_annotations(self):
        if not self._annotations_exist():
            try:
                print("Downloading COCO annotations...")
                annotations_zip_content = urlopen(self._annotations_archive_url.format(self.__annotations_year)).read()
                annotations_zip_file = ZipFile(io.BytesIO(annotations_zip_content))
                annotations_zip_file.extractall(self.__dataset_path)
            except Exception as e:
                raise Exception(f"{e}\nFailed to download COCO annotations. Try to run code one more time")
            else:
                print("COCO annotations downloaded!")
