import yaml
from argparse import ArgumentParser
from coco_toolkit.utils.files import get_categories_from_txt


class ConfigArgumentsParser:
    _config_args_parser = ArgumentParser()
    _config_args_parser.add_argument("--dataset_path",
                                     type=str,
                                     default="../Dataset",
                                     help="Path where the dataset folder is placed",
                                     )
    _config_args_parser.add_argument("--categories_path",
                                     type=str,
                                     required=True,
                                     help="Path where the categories.txt is placed"
                                     )
    _config_args_parser.add_argument("--labels",
                                     type=str,
                                     required=True,
                                     help="Type of the labels to generate"
                                     )
    _config_args_parser.add_argument("--annotations_year",
                                     type=int,
                                     default=2017,
                                     help="Year of the annotations to download"
                                     )
    _config_args_parser.add_argument("--multiclass",
                                     type=str,
                                     default=None,
                                     help="If multiclass is needed"
                                     )

    _available_labels = ("yolo",)
    _available_ants_years = (2017,)

    def _arguments_are_correct(self, config_args):
        return config_args["labels"] in self._available_labels and \
               config_args["annotations_year"] in self._available_ants_years

    def parse_arguments(self):
        config_args = vars(self._config_args_parser.parse_args())
        if self._arguments_are_correct(config_args):
            return config_args
        raise Exception("Check config arguments for correctness")


class ConfigYAMLGenerator:
    def __init__(self, config_args, config_yaml_file_path):
        self._config_yaml_file_path = config_yaml_file_path
        self._config_args = config_args

    def generate_yaml_file(self):
        categories = get_categories_from_txt(self._config_args["categories_path"])
        del self._config_args["categories_path"]

        self._config_args["categories"] = categories

        with open(self._config_yaml_file_path, "w") as config_yaml_file:
            _ = yaml.dump(data=self._config_args, stream=config_yaml_file)


def main():
    config_args_parser = ConfigArgumentsParser()
    config_args = config_args_parser.parse_arguments()

    config_yaml_file_path = "coco_toolkit/config_files/dataset_config.yaml"
    config_yaml_generator = ConfigYAMLGenerator(config_args, config_yaml_file_path)
    config_yaml_generator.generate_yaml_file()


if __name__ == '__main__':
    main()

# python configure.py --dataset_path ../Animals --categories_path ../Animals/categories.txt

