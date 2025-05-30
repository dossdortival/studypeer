from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    bio = models.TextField(_('bio'), blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    interests = models.CharField(_('interests'), max_length=255, blank=True)
    location = models.CharField(_('location'), max_length=100, blank=True)
    
    def __str__(self):
        return self.username

class Subject(models.Model):
    name = models.CharField(_('name'), max_length=100, unique=True)
    description = models.TextField(_('description'), blank=True)
    
    def __str__(self):
        return self.name

class StudyGroup(models.Model):
    title = models.CharField(_('title'), max_length=100, unique=True, default='Untitled Group')
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
        return self.title
    
    def current_member_count(self):
        return self.memberships.count()
    
    def is_full(self):
        return self.current_member_count() >= self.max_members
    
class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memberships')
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='memberships')
    joined_at = models.DateTimeField(_('joined at'), auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'group')
    
    def __str__(self):
        return f"{self.user.username} in {self.group.title}"