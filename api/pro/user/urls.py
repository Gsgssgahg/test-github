from django.urls import path
from .views import ListAPiView,CreateAPiView

urlpatterns = [
    path('/listapi',ListAPiView.as_view()),
    path('/createapi',CreateAPiView.as_view())
]

