from os.path import exists as path_exists
from os.path import join as join_path
from .image_params_getters import ImageAnnotationGetter, ImagesInformationGetter


class YOLOLabelGenerator:
    __dataset_parts = ('val', 'train')
    _image_annotation_getter = ImageAnnotationGetter()
    _images_info_getter = ImagesInformationGetter()

    def __init__(self, dataset_path, categories, multiclass):
        self.__images_folder_path = join_path(dataset_path, "images")
        self.__labels_folder_path = join_path(dataset_path, "labels")
        self.__dataset_path = dataset_path
        self.__categories = categories
        self.__multiclass = multiclass

    @staticmethod
    def _clean_file_content(file_path):
        with open(file_path, "w"): pass

    @staticmethod
    def _convert_bbox_coco2yolo(image_size, coco_bbox):
        # convert to (x1, y1, x2, y2)
        kitti_bbox = (coco_bbox[0], coco_bbox[1],
                      coco_bbox[2] + coco_bbox[0], coco_bbox[3] + coco_bbox[1])

        x_min, x_max = sorted((kitti_bbox[0], kitti_bbox[2]))
        y_min, y_max = sorted((kitti_bbox[1], kitti_bbox[3]))

        dw = 1.0 / image_size[1]
        dh = 1.0 / image_size[0]
        norm_x = round(((x_max + x_min) / 2.0) * dw, 6)
        norm_y = round(((y_max + y_min) / 2.0) * dh, 6)
        norm_w = round((x_max - x_min) * dw, 6)
        norm_h = round((y_max - y_min) * dh, 6)

        return norm_x, norm_y, norm_w, norm_h

    def _write_label_to_txt_file(self, label_file_path, category_number, image_size, coco_bbox):
        yolo_bbox = self._convert_bbox_coco2yolo(image_size, coco_bbox)
        labels_file_content = "{} {} {} {} {}\n".format(category_number,
                                                        yolo_bbox[0], yolo_bbox[1],
                                                        yolo_bbox[2], yolo_bbox[3])

        with open(label_file_path, "a") as labels_file:
            labels_file.write(labels_file_content)

    def _convert_and_write_labels(self, labels_folder_path, dataset_part,
                                  image_info, category_number, category_id):
        image_size = image_info['height'], image_info['width']
        image_annotations = self._image_annotation_getter.get_image_annotations(dataset_part=dataset_part,
                                                                                image_id=image_info['id'],
                                                                                category_id=category_id,
                                                                                iscrowd=None)
        label_file_name = f"{image_info['file_name'].split('.')[0]}.txt"
        label_file_path = join_path(labels_folder_path, label_file_name)
        self._clean_file_content(label_file_path)

        for object_annotation in image_annotations:
            coco_bbox = object_annotation['bbox']
            self._write_label_to_txt_file(label_file_path, category_number, image_size, coco_bbox)

    @staticmethod
    def _image_is_in_images_folder(dataset_part_images_path, image_name):
        return path_exists(join_path(dataset_part_images_path, image_name))

    def _generate_labels_for_dataset_part(self, dataset_part):
        dataset_part_images_path = join_path(self.__images_folder_path, dataset_part)
        dataset_part_labels_path = join_path(self.__labels_folder_path, dataset_part)

        category_number = 0
        for category in self.__categories:
            category_id = self._image_annotation_getter.get_category_id(dataset_part, category)
            images_info = self._images_info_getter.get_images_info(dataset_part, category)
            for image_info in images_info:
                if self._image_is_in_images_folder(dataset_part_images_path, image_info["file_name"]):
                    self._convert_and_write_labels(dataset_part_labels_path, dataset_part,
                                                   image_info, category_number, category_id)
            if not self.__multiclass:
                category_number += 1

    def generate_labels(self):
        print("Generating YOLO labels...")
        for dataset_part in self.__dataset_parts:
            self._generate_labels_for_dataset_part(dataset_part)
        print("YOLO labels generated!")
