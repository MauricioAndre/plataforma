from django.urls import path
from . import views

urlpatterns = [
    path('uploadxml/', views.upload_xml, name='upload_xml'),
]
