from coco_toolkit.modules.coco_images_downloader import COCOImagesDownloader


def download_coco_images(config_yaml_params, run_args):
    dataset_path = config_yaml_params["dataset_path"]
    categories = config_yaml_params["categories"]
    train_images = run_args["train"]
    val_images = run_args["val"]
    web_batch_size = run_args["web_batch"]
    coco_downloader = COCOImagesDownloader(dataset_path, categories, train_images, val_images, web_batch_size)
    coco_downloader.download_images()



