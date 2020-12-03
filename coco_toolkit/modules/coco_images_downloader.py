import grequests
from tqdm import tqdm
from itertools import combinations
from os.path import exists as path_exists
from os.path import join as join_paths
from .image_params_getters import ImagesInformationGetter


class COCOImagesDownloader:
    __dataset_parts = ('val', 'train')
    _images_info_getter = ImagesInformationGetter()

    def __init__(self, dataset_path, categories, train_images, val_images, batch_size):
        self.__images_folder_path = join_paths(dataset_path, "images")
        self.__labels_folder_path = join_paths(dataset_path, "labels")
        self.__dataset_path = dataset_path
        self.__categories = categories
        self.__amount_of_train_images = train_images
        self.__amount_of_val_images = val_images
        self.__batch_size = batch_size

    @staticmethod
    def _write_image(image_path, image_content):
        with open(image_path, "wb") as binary_image_writer:
            binary_image_writer.write(image_content)

    @staticmethod
    def _filter_by_existence(dataset_part_images_path, images_info):
        filtered_images_info = list()
        for image_name_url in images_info:
            image_path = join_paths(dataset_part_images_path, image_name_url[0])
            if not path_exists(image_path):
                filtered_images_info.append(image_name_url)
        return filtered_images_info

    def _download_and_write_batch_of_images(self, dataset_part_images_path, images_info):
        keys = ("file_name", "coco_url")
        image_names_urls = (list(map(image_info.get, keys)) for image_info in images_info)
        image_names_urls = self._filter_by_existence(dataset_part_images_path, image_names_urls)
        image_names = map(lambda name_url: name_url[0], image_names_urls)
        image_urls = map(lambda name_url: name_url[1], image_names_urls)
        async_requests = (grequests.get(image_url) for image_url in image_urls)
        responses = grequests.map(async_requests)

        for image_name, response in zip(image_names, responses):
            try:
                image_content = response.content
                image_path = join_paths(dataset_part_images_path, image_name)
                self._write_image(image_path, image_content)
            except Exception:
                pass

    @staticmethod
    def _get_part_of_images_info(images_info, amount_of_images):
        if len(images_info) > amount_of_images:
            return images_info[:amount_of_images]
        return images_info

    def _download_images_for_dataset_part(self, dataset_part, amount_of_images):
        dataset_part_images_path = join_paths(self.__images_folder_path, dataset_part)
        for category in self.__categories:
            all_images_info = self._images_info_getter.get_images_info(dataset_part, category)
            part_of_images_info = self._get_part_of_images_info(all_images_info, amount_of_images)
            for idx in tqdm(range(0, len(part_of_images_info), self.__batch_size),
                            desc=f"Downloading {dataset_part} set, {category} images, batch={self.__batch_size}",
                            unit=" batches"):
                batch_of_images_info = part_of_images_info[idx:idx + self.__batch_size]
                self._download_and_write_batch_of_images(dataset_part_images_path, batch_of_images_info)

    def download_images(self):
        if self.__amount_of_val_images:
            self._download_images_for_dataset_part("val", self.__amount_of_val_images)
        if self.__amount_of_train_images:
            self._download_images_for_dataset_part("train", self.__amount_of_train_images)
