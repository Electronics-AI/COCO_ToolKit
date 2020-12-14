# COCO ToolKit
This repository presents the COCO ToolKit code and tutorials for ease-of-use.
COCO ToolKit provides the following options:
* Download **any number of categories** from COCO dataset
* Download **any number of images per category** (considering limits of COCO dataset, sure)
* Generate **labels** for images in **YOLO format** (Mask R-CNN and One-Hot in near future)
* Training **YOLOv5 on custom dataset** support
## 1.0 Getting Started
### 1.1 Installation
**Installation on Windows or Linux** (Tested on Windows 10, Linux Ubuntu 18.04)
1. Clone this repository locally:
```
git clone https://github.com/Electronics-AI/COCO_ToolKit.git
```
2. Install the requirements:
```
pip install -r requirements.txt
```
3. Download and install pycocotools:
```
pip install -U git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
``` 
**Installation in Google Colab** (Tested in Google Colab)
1. Clone this repository locally:
```
!git clone https://github.com/Electronics-AI/COCO_ToolKit.git
```
2. Download and install pycocotools:
```
!pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
``` 
3. Install the Google Colab requirements:
```
!pip install -r colab_requirements.txt
```

## 2.0 Configuring
1. Create your dataset folder and categories.txt file. Let's for instance create an Animals dataset near the
COCO_ToolKit folder and suppose our dataset contains 4 categories: dog, cat, bear and bird. 
My categories.txt file will look like this:
```
dog
cat
bear
bird
```  
And here is my directory structure:
```
|                                               
|---Animals
|          categories.txt
|---COCO_ToolKit
               coco_toolkit/
               colab_requirements.txt
               configure.py
               LICENSE
               ...
```                                                 
2. Configure your dataset (You must be in the COCO_Toolkit directory)
```
python configure.py --dataset_path {dataset folder path} --categories_path {categories.txt path} --labels {labels to generate}
``` 
For my directory structure configuration looks so:
```
python configure.py --dataset_path ../Animals --categories_path ../Animals/categories.txt --labels yolo
```

## 3.0 Running
1. Let's run our code!
```
python run.py --all --train {images per category in the train set to download} \
                    --val {images per category in the validation set to download} \
                    --web_batch {download images at once from COCO website}
```
**Note:** --all argument is responsible for:
* Dataset directory structure generation (labels, images, train, val folders) 
* Downloading annotations from the COCO website
* Downloading images from the COCO website
* Labels generation   

For my dataset I want to:
* Download 1000 images per category in the train set ("--train 1000" argument)
* Download all images per category in the validation set ("--val -1 argument", -1 means download all the images)
* I have a good internet connection, so let's set the batch of images to download = 20 ("--web_batch 20" argument)  
My run.py start looks like this:
```
python run.py --all --train 1000 --val -1 --web_batch 20
```
*Wait until run.py finishes it's work and you are ready to use your custom COCO dataset!*

## 4.0 More Information
For more information, such as training YOLOv5 in Google Colab with COCO ToolKit, see the
docs folder.