from django.contrib import admin

# Register your models here.
from .models import Member, Lab, Subgroup, Project, Announcement, ExecutiveRelationship

admin.site.register(Member)
admin.site.register(Lab)
admin.site.register(Subgroup)
admin.site.register(Project)
admin.site.register(Announcement)
admin.site.register(ExecutiveRelationship)