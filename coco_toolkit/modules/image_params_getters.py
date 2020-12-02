from pycocotools.coco import COCO
from ..utils.files import get_annotations_file_path
from ..utils.files import get_config_yaml_params


class ImageParametersGetter:
    __config_yaml_parameters = get_config_yaml_params()
    __train_coco_manager = COCO(get_annotations_file_path(__config_yaml_parameters["dataset_path"],
                                                          'instances_train',
                                                          __config_yaml_parameters["annotations_year"]))
    __val_coco_manager = COCO(get_annotations_file_path(__config_yaml_parameters["dataset_path"],
                                                        'instances_val',
                                                        __config_yaml_parameters["annotations_year"]))
    __annotations_year = str(__config_yaml_parameters["annotations_year"])

    def _choose_coco_manager(self, dataset_part):
        return self.__train_coco_manager if dataset_part == 'train' else self.__val_coco_manager


class ImageAnnotationGetter(ImageParametersGetter):
    def get_category_id(self, dataset_part, category):
        coco_manager = self._choose_coco_manager(dataset_part)

        return coco_manager.getCatIds(catNms=[category])

    def get_image_annotations(self, dataset_part, image_id, category_id, iscrowd):
        coco_manager = self._choose_coco_manager(dataset_part)
        annotation_id = coco_manager.getAnnIds(imgIds=image_id, catIds=category_id, iscrowd=iscrowd)

        return coco_manager.loadAnns(annotation_id)


class ImagesInformationGetter(ImageParametersGetter):
    def get_images_info(self, dataset_part, category):
        coco_manager = self._choose_coco_manager(dataset_part)
        category_id = coco_manager.getCatIds(catNms=[category])
        image_ids = coco_manager.getImgIds(catIds=category_id)

        return coco_manager.loadImgs(ids=image_ids)