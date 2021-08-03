## Location
```shell
~/Web/TestWeb/...
```
## Object Detection
需要安装Object Detection相关的Python包
```shell
# 运行程序会提示缺少的Python包
pip3 install xxx
```
编译和Tensorflow Object Detection API的安装
```shell
# git clone.
git clone https://github.com/tensorflow/models.git
cd models/research
# Compile protos.
protoc object_detection/protos/*.proto --python_out=.
# Install TensorFlow Object Detection API.
cp object_detection/packages/tf2/setup.py .
python -m pip install --use-feature=2020-resolver .
# Test
python object_detection/builders/model_builder_tf2_test.py
```

## Web Server
```shell
# Run Web Server
python3 manage.py runserver
# upload image for process
curl -F "file=@./COCO_test2014_000000000014.jpg;filename='COCO_test2014_000000000014.jpg'" http://localhost:8000/
```