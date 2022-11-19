import os
import re

from utils import recreate_dir, get_files, create_dir_if_not_exists
from yolo_scripts import predict_yolov5


def prepare_report(path_to_images):
    with open(os.path.join(REPORTS_PATH, f'report_{YOLO_MODEL}.csv'), 'w') as report:
        for image_path in get_files(path_to_images):
            if image_path[0] == '.':
                continue
            car_color = re.findall(r'\d+_crop_([^_]+)_.jpg', image_path)[0]
            report.write(f'{car_color}\n')


CROPPED_TEST_DATASET_PATH = 'cropped_test_data'
PREDICTED_TEST_DATASET_PATH = 'predicted_test_data'
REPORTS_PATH = 'reports'
YOLO_MODEL = 'best_resnet50_1711_v2.pt'

recreate_dir(PREDICTED_TEST_DATASET_PATH)
create_dir_if_not_exists(REPORTS_PATH)
os.system(predict_yolov5(CROPPED_TEST_DATASET_PATH, PREDICTED_TEST_DATASET_PATH, YOLO_MODEL))
prepare_report(PREDICTED_TEST_DATASET_PATH)
