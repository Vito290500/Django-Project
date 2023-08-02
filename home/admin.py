from django.contrib import admin

# Register your models here.
from .models import ProjectStorage, MySkill, MyUpdateContact

admin.site.register(ProjectStorage)
admin.site.register(MySkill)
admin.site.register(MyUpdateContact)