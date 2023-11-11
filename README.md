# YOLOv8 + Tracking Object Dectection


## Introduction

In computer vision and object detection, YOLO (You Only Look Once) has become a popular real-time object detection algorithm.[YOLOv8](https://github.com/ultralytics/ultralytics), an evolution of the YOLO series, introduces improvements in accuracy and speed, making it a powerful tool for various applications.

This document focuses on combining YOLOv8 with object tracking techniques to enhance the capabilities of object detection in video streams. Object tracking enables the tracking of detected objects across consecutive frames, providing valuable information for applications like surveillance, autonomous vehicles, and more.


## Features
- Object detection
- Multiple input formats
- Multiple Object Tracking and Counting.
## Installation
### Create a virtual environment
```commandline
# create
python -m venv test_env

# activate
source test_env/bin/activate
```

### Clone repository
```commandline
git clone https://github.com/hiepdaoquang704/website-object-detection.git
cd website-object-detection
```

### Install packages
```commandline
# Dependencies
pip install -r requirments.txt
```
### Download Pre-trained YOLOv8 Detection Weights
The weight files can be downloaded automatic from the table below.

| Model                                                                                | size<br><sup>(pixels) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
| ------------------------------------------------------------------------------------ | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ----------------- |
| [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt) | 640                   | 37.3                 | 80.4                           | 0.99                                | 3.2                | 8.7               |
| [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt) | 640                   | 44.9                 | 128.4                          | 1.20                                | 11.2               | 28.6              |
| [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m.pt) | 640                   | 50.2                 | 234.7                          | 1.83                                | 25.9               | 78.9              |
| [YOLOv8l](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8l.pt) | 640                   | 52.9                 | 375.2                          | 2.39                                | 43.7               | 165.2             |
| [YOLOv8x](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt) | 640                   | 53.9                 | 479.1                          | 3.53                                | 68.2               | 257.8             |


## Run
```commandline
streamlit run main.py
```
Then will start the Streamlit server and open your web browser to the default Streamlit page automatically.
You must register account and login to redirect to my dashboard.Everything is fast.

## Result

![alt text](images/1.jpg "Log in")
![alt text](images/2.jpg "Log out")
![alt text](images/3.jpg "Dashboard and result")

## Acknowledgement
- https://github.com/ultralytics/ultralytics
- https://github.com/streamlit/streamlit
- https://github.com/ZQPei/deep_sort_pytorch
