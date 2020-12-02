from argparse import ArgumentParser
from coco_toolkit.utils.files import get_config_yaml_params


class RunArgumentsParser:
    _run_arguments_parser = ArgumentParser()
    _run_arguments_parser.add_argument("--all",
                                       action="store_true",
                                       help="Run all the scripts"
                                       )
    _run_arguments_parser.add_argument("--make_dirs",
                                       action="store_true",
                                       help="Generate the dataset dir structure"
                                       )
    _run_arguments_parser.add_argument("--generate_yaml",
                                       action="store_true",
                                       help="Generate the dataset yaml file"
                                       )
    _run_arguments_parser.add_argument("--download_annotations",
                                       action="store_true",
                                       help="Download coco annotations from the coco website"
                                       )
    _run_arguments_parser.add_argument("--download_images",
                                       action="store_true",
                                       help="Download coco images from the coco website"
                                       )
    _run_arguments_parser.add_argument("--train",
                                       type=int,
                                       default=0,
                                       help="Amount of train images per category to download"
                                       )
    _run_arguments_parser.add_argument("--val",
                                       type=int,
                                       default=0,
                                       help="Amount of val images per category to download"
                                       )
    _run_arguments_parser.add_argument("--batch",
                                       type=int,
                                       default=15,
                                       help="Batch of images to download from COCO website at once."
                                            "By default it's 15, but if you have fast internet"
                                            "connection, you can choose higher value")

    def parse_arguments(self):
        run_args = vars(self._run_arguments_parser.parse_args())
        return run_args


def execute_scripts():
    run_args_parser = RunArgumentsParser()
    run_arguments = run_args_parser.parse_arguments()
    config_yaml_params = get_config_yaml_params()

    if run_arguments["all"] or run_arguments["make_dirs"]:
        from coco_toolkit.scripts.make_dataset_dir_structure import make_dirs
        make_dirs(config_yaml_params)

    if run_arguments["all"] or run_arguments["generate_yaml"]:
        from coco_toolkit.scripts.generate_dataset_yaml import generate_yaml
        generate_yaml(config_yaml_params)

    if run_arguments["all"] or run_arguments["download_annotations"]:
        from coco_toolkit.scripts.download_coco_annotations import download_coco_annotations
        download_coco_annotations(config_yaml_params)

    if run_arguments["all"] or run_arguments["download_images"]:
        from coco_toolkit.scripts.download_coco_images import download_coco_images
        download_coco_images(config_yaml_params, run_arguments)

    if config_yaml_params["labels"] == "yolo":
        from coco_toolkit.scripts.generate_yolo_labels import generate_yolo_labels
        generate_yolo_labels(config_yaml_params)


if __name__ == "__main__":
    execute_scripts()
