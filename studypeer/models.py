from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    bio = models.TextField(_('bio'), blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    university = models.CharField(_('university'), max_length=100, blank=True)
    
    def __str__(self):
        return self.username

class Subject(models.Model):
    name = models.CharField(_('name'), max_length=100)
    code = models.CharField(_('code'), max_length=20, blank=True)
    description = models.TextField(_('description'), blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.code})" if self.code else self.name

class StudyGroup(models.Model):
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='groups')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField(User, related_name='study_groups')
    meeting_times = models.JSONField(_('meeting times'), default=list)
    location = models.CharField(_('location'), max_length=200)
    max_members = models.PositiveIntegerField(_('max members'), default=10)
    is_active = models.BooleanField(_('is active'), default=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject.name}"
    
    def available_slots(self):
        return self.max_members - self.members.count()