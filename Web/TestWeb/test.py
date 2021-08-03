import os

def traverseDir(dir):
    image_list = []
    for file in os.listdir(dir):
        file = "../../upload/" + file
        image_list.append(file)
    return image_list

dir = "app01/upload"

print(traverseDir(dir))