from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Skill)
admin.site.register(Batch)