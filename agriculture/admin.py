from unittest import mock
from django.contrib import admin
from .models import Agriculture, AgricultureType

admin.site.register(Agriculture)
admin.site.register(AgricultureType)
