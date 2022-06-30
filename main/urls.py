from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('docker/', views.MainDockerView.as_view(), name='dockerview'),
    path('docker/add', views.DockerAddView.as_view(), name='dockeradd')
]