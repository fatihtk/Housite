from django.contrib import admin

from . models import Houses
admin.site.register(Houses)

from . models import post
admin.site.register(post)