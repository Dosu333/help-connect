from django.db import models
from django.contrib.auth import get_user_model
import uuid


class BaseClass(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class CommunityAlert(BaseClass):
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    media = models.FileField(upload_to='communityalerts/', blank=True, null=True)
    is_reported = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    flagged_by = models.ManyToManyField(get_user_model(), blank=True, related_name='flaggers')
    reported_by = models.ManyToManyField(get_user_model(), blank=True, related_name='reporters')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.first_name + ' ' + self.author.last_name