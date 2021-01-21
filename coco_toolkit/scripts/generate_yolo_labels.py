from coco_toolkit.modules.label_generators import YOLOLabelGenerator


def generate_yolo_labels(config_yaml_params):
    dataset_path = config_yaml_params["dataset_path"]
    categories = config_yaml_params["categories"]
    multiclass = config_yaml_params["multiclass"]
    yolo_label_generator = YOLOLabelGenerator(dataset_path, categories, multiclass)
    yolo_label_generator.generate_labels()

