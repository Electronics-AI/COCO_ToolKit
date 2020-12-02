from coco_toolkit.modules.dataset_yaml_generator import DatasetYAMLGenerator


def generate_yaml(config_yaml_params):
    dataset_path = config_yaml_params["dataset_path"]
    categories = config_yaml_params["categories"]
    multiclass = config_yaml_params["multiclass"]
    yaml_generator = DatasetYAMLGenerator(dataset_path, categories, multiclass)
    yaml_generator.generate_dataset_yaml()

