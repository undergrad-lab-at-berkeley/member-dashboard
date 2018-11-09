from django.contrib import admin

# Register your models here.
from .models import Member, Department, Lab, Announcement

admin.site.register(Member)
admin.site.register(Department)
admin.site.register(Lab)
admin.site.register(Announcement)