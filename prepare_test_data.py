import os
import re

from utils import recreate_dir
from yolo_scripts import detect_yolov7

TEST_DATASET_PATH = 'test_data'
CROPPED_TEST_DATASET_PATH = 'cropped_test_data'
YOLO7_DETECT_MODEL = 'yolov7.pt'

recreate_dir(CROPPED_TEST_DATASET_PATH)
os.system(detect_yolov7(TEST_DATASET_PATH, CROPPED_TEST_DATASET_PATH,
                        YOLO7_DETECT_MODEL))
