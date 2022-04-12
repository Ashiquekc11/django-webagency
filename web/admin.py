import imp
from operator import concat
from django.contrib import admin
from .models import Contact, Blog

# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog)