import yaml
from os.path import join as join_paths
from os.path import exists as path_exists


def get_config_yaml_params():
    config_yaml_file_path = "coco_toolkit/config_files/dataset_config.yaml"
    with open(config_yaml_file_path, "r") as config_yaml_file:
        return yaml.load(config_yaml_file, Loader=yaml.FullLoader)


def get_categories_from_txt(categories_txt_path):
    category_names = ("person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck",
                          "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
                          "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
                          "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
                          "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
                          "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana",
                          "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake",
                          "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse",
                          "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
                          "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush")

    with open(categories_txt_path, "r") as categories_file:
        # get all categories from txt
        categories = [category.rstrip().lower() for category in categories_file]

        # check if categories exist
        existence_list = [cat in category_names for cat in categories]
        if all(existence_list):
            return categories

        # if there is(are) nonexistent category(ies) in categories.txt file
        nonexistent_categories_lines = [index for index, exists in enumerate(existence_list) if not exists]
        raise Exception("Nonexistent categories found in categories.txt file."
                        f"Check categories in line(s) {nonexistent_categories_lines} for correctness")


def get_annotations_file_path(dataset_path, annotations_type, annotations_year):
    annotations_folder_path = join_paths(dataset_path, "annotations")
    annotations_file_path = join_paths(annotations_folder_path,
                                         f"{annotations_type}{str(annotations_year)}.json")
    if path_exists(annotations_file_path):
        return annotations_file_path
    raise Exception(f"Cannot find the {annotations_file_path} file")

