from django.contrib import admin
# Register your models here
from .models import Book,IssuedItem,Student

admin.site.register(Book)
admin.site.register(IssuedItem)
admin.site.register(Student)