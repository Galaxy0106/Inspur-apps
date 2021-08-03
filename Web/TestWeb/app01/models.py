from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20)
    headImg = models.ImageField(upload_to='media/research/object_detection/test_images')