from django.urls import path
from .views import BookListApiView,BookCreateAPiView

urlpatterns = [
    path('/listapi', BookListApiView.as_view()),
    path('/createapi',BookCreateAPiView.as_view()),
]
