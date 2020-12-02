import os
from os.path import join as join_paths


class DatasetDirStructureMaker:
    __dataset_parts = ('val', 'train')

    def __init__(self, dataset_path):
        self.__dataset_path = self._set_dataset_path(dataset_path)

    @staticmethod
    def _set_dataset_path(dataset_path):
        os.makedirs(dataset_path, exist_ok=True)
        return dataset_path

    def make_dataset_dir_tree(self):
        os.makedirs(join_paths(self.__dataset_path, "annotations"), exist_ok=True)

        for dataset_part_folder_name in self.__dataset_parts:
            os.makedirs(join_paths(self.__dataset_path, f"images/{dataset_part_folder_name}"), exist_ok=True)
            os.makedirs(join_paths(self.__dataset_path, f"labels/{dataset_part_folder_name}"), exist_ok=True)

