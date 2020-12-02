from coco_toolkit.modules.dataset_yaml_generator import DatasetYAMLGenerator


def generate_dataset_yaml(config_args):
    dataset_path = config_args["dataset_path"]
    categories = config_args["categories"]
    multiclass = config_args["multiclass"]
    yaml_generator = DatasetYAMLGenerator(dataset_path, categories, multiclass)
    yaml_generator.generate_dataset_yaml()

