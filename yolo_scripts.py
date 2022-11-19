import os


def predict_yolov5(input_path, output_path, yolo_model):
    return f'python yolov5/classify/predict.py ' \
           f'--weights weights/{yolo_model} ' \
           f'--img-size 224 ' \
           f'--source {input_path} ' \
           f'--save-dir {output_path} '


def detect_yolov7(input_path, output_path, yolo_model):
    if not os.path.exists(os.path.join('yolov7', yolo_model)):
        os.system(f'wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/{yolo_model} '
                  f'-O {os.path.join("yolov7", yolo_model)}')
    return f'python {os.path.join("yolov7", "detect.py")} ' \
           f'--weights {os.path.join("yolov7", yolo_model)} ' \
           f'--img-size 256 ' \
           f'--source {input_path} ' \
           f'--save-dir {output_path} '
