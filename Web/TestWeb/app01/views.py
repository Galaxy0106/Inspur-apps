import os
import shutil
from TestWeb.settings import IMAGE_LIST, IMAGE_RESULT_LIST
from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from .models import user
from django.views.decorators.csrf import csrf_exempt
from media.research.object_detection import  object_detection_spyder_test as ods

def debug(arg):
    print("-----------log begin------------")
    print(arg)
    print("------------log end-------------")

def file_copy(name):
    old_path = "/home/sz/Web/TestWeb/media/research/object_detection/test_images/" + name
    new_path = "/home/sz/Web/TestWeb/app01/static/" + name
    shutil.copyfile(old_path, new_path)

# def traverseDir(dir):
#     image_list = []
#     for file in os.listdir(dir):
#         if dir == "/home/sz/Web/TestWeb/media/research/object_detection/test_image_results":
#             file = "result/" + file
#         image_list.append(file)
#     return image_list

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(required=False)
    headImg = forms.ImageField(required=False)

@csrf_exempt
def index(request):
    context = {}
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            # Upload
            User = user(headImg=request.FILES['file'])
            User.save()
            print('upload ok!\n')
            # Add to list
            name = str(User.headImg).split('/')[-1]
            IMAGE_LIST.append(name)
            # Copy to static
            file_copy(name)
            # Process Image
            result_name = "result/" + ods.main(name)
            # Add to list
            IMAGE_RESULT_LIST.append(result_name)
            # Copy to static
            file_copy(result_name)
    # unprocessed_file_dir = r'/home/sz/Web/TestWeb/media/research/object_detection/test_images'
    # processed_file_dir = r'/home/sz/Web/TestWeb/media/research/object_detection/test_image_results'

    # image1_list = traverseDir(unprocessed_file_dir)
    # image2_list = traverseDir(processed_file_dir)
    print(IMAGE_LIST)
    print(IMAGE_RESULT_LIST)

    context["image1_list"] = IMAGE_LIST
    context["image2_list"] = IMAGE_RESULT_LIST
    # print(context)
    return render(request, "app01/index.html", context)