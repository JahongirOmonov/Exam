from django.contrib import admin
from .models import authorModel, bookModel

# Register your models here.

admin.site.register(authorModel)
admin.site.register(bookModel)
