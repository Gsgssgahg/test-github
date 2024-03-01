from django.urls import path
from .views import *

urlpatterns = [
    path('/listapi', ListAPiView.as_view()),
    path('/createapi', CreateAPiView.as_view()),
    path('/deleteapi',DeleteAPiView.as_view()),
    path('/updateapi',UpdateAPiView.as_view()),
]