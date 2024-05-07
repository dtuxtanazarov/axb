from django.contrib import admin
from .models import Message, Person
# Register your models here.
admin.site.register(Message)
admin.site.register(Person)