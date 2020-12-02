from coco_toolkit.modules.dataset_dir_structure_maker import DatasetDirStructureMaker


def make_dirs(config_yaml_params):

    dataset_path = config_yaml_params["dataset_path"]
    dir_generator = DatasetDirStructureMaker(dataset_path)
    dir_generator.make_dataset_dir_tree()

