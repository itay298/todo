from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext as _
# Create your models here.

user = get_user_model()

class TodoNote(models.Model):
    author = models.ForeignKey(user, models.CASCADE, related_name='todos')
    title = models.CharField(_('Update todo note'), max_length=255)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    created_at = models.DateTimeField(_('updated at'), auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse("todo:index")
    
    
    def __str__(self):
        return self.title
    