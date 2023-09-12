from django.db import models
from datetime import datetime


# Create your models here.


class authorModel(models.Model):
    name=models.CharField(max_length=100, default='')
    surname=models.CharField(max_length=100, default='')
    date_of_birth=models.DateTimeField(default=datetime.now)

    class Meta:
        db_table='author'

    def __str__(self) -> str:
        return self.name
    

class bookModel(models.Model):
    name=models.CharField(max_length=100, default='')
    page=models.PositiveIntegerField(default=3)
    year_of_invented=models.DateTimeField(default=datetime.now)
    author=models.ForeignKey(authorModel, on_delete=models.CASCADE)
    

    class Meta:
        db_table='book'

    def __str__(self) -> str:
        return self.name

