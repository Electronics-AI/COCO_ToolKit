import os
import yaml
from os.path import join as join_path


class DatasetYAMLGenerator:
    __dataset_parts = ('val', 'train')
    __yaml_file_name = "dataset.yaml"

    def __init__(self, dataset_path, categories, multiclass):
        self.__dataset_path = dataset_path
        self.__categories = categories
        self.__multiclass = multiclass
        self.__yaml_file_path = join_path(dataset_path, self.__yaml_file_name)

    def _append_paths_to_yaml(self):
        for dataset_part in self.__dataset_parts:
            dataset_part_path = f"{join_path(self.__dataset_path, 'images', dataset_part).replace(os.sep, '/')}/"
            path = {dataset_part: dataset_part_path}
            with open(self.__yaml_file_path, "a") as yaml_file:
                _ = yaml.dump(data=path, stream=yaml_file)

    def _append_nc_to_yaml(self):
        nc = {"nc": 1 if self.__multiclass else len(self.__categories)}
        with open(self.__yaml_file_path, "a") as yaml_file:
            _ = yaml.dump(data=nc, stream=yaml_file)

    def _append_names_list_to_yaml(self):
        with open(self.__yaml_file_path, "a") as yaml_file:
            yaml_file.write("names: [")
            if self.__multiclass:
                yaml_file.write(f"'{self.__multiclass}'")
            else:
                for category in self.__categories:
                    yaml_file.write(f"'{category}', ")
            yaml_file.write("]")

    def generate_dataset_yaml(self):
        with open(self.__yaml_file_path, "w"): pass
        self._append_paths_to_yaml()
        self._append_nc_to_yaml()
        self._append_names_list_to_yaml()