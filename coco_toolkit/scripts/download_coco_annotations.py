from coco_toolkit.modules.coco_annotations_downloader import COCOAnnotationsDownloader


def download_coco_annotations(config_yaml_params):
    dataset_path = config_yaml_params["dataset_path"]
    annotations_year = config_yaml_params["annotations_year"]
    ants_downloader = COCOAnnotationsDownloader(dataset_path, annotations_year)
    ants_downloader.download_annotations()

