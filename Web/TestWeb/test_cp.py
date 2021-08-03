import shutil

def file_copy(name):
    old_path = "/home/sz/Web/TestWeb/media/research/object_detection/test_images/" + name
    new_path = "/home/sz/Web/TestWeb/app01/static/" + name
    shutil.copyfile(old_path, new_path)

file_copy("COCO_test2014_000000000001.jpg")
file_copy("result/COCO_test2014_000000000001_result.jpg")