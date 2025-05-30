from django.contrib import admin
from .models import User, Subject, StudyGroup, Membership


admin.site.register(User)
admin.site.register(Subject)
admin.site.register(StudyGroup)
admin.site.register(Membership)
