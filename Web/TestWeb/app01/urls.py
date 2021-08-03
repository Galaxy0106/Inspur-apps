from django.urls import path
from . import views
from django.conf.urls.static import static

# 将url传入view.index模块中， index类别名name
urlpatterns = [
    path(r'', views.index, name='index'), 
]