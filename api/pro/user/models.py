from django.db import models


class ApiModel(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=30)
    age = models.IntegerField(max_length=120)

    def __str__(self):
        return self.name
