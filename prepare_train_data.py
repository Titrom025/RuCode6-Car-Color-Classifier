import os

from utils import recreate_dir, get_files, get_dirs
from yolo_scripts import detect_yolov7


TRAIN_DATASET_PATH = 'car_color_dataset/train'
CROPPED_TRAIN_DATASET_PATH = 'cropped_train'
YOLO7_DETECT_MODEL = 'yolov7.pt'

recreate_dir(CROPPED_TRAIN_DATASET_PATH)
for color_dir in get_dirs(TRAIN_DATASET_PATH):
    print(f'Folder: {color_dir} - {len(get_files(os.path.join(TRAIN_DATASET_PATH, color_dir)))} files')

    input_path = os.path.join(TRAIN_DATASET_PATH, color_dir)
    output_path = os.path.join(CROPPED_TRAIN_DATASET_PATH, color_dir)

    os.system(detect_yolov7(input_path, output_path,
                            YOLO7_DETECT_MODEL))

