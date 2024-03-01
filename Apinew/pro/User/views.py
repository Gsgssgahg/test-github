from django.shortcuts import render
from rest_framework import generics
from .models import ApiModel
from .serializers import APiSerializer
from rest_framework.views import APIView

class ListAPiView(generics.ListAPIView):
    queryset = ApiModel.objects.all()
    serializer_class = APiSerializer

class CreateAPiView(generics.CreateAPIView):
    queryset = ApiModel.objects.all()
    serializer_class = APiSerializer

class DeleteAPiView(generics.DestroyAPIView):
    queryset = ApiModel.objects.all()
    serializer_class = APiSerializer

class UpdateAPiView(generics.UpdateAPIView):
    queryset = ApiModel.objects.all()
    serializer_class = APiSerializer
