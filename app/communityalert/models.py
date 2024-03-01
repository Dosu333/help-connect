from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class CommunityAlert(BaseModel):
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    media = models.FileField(
        upload_to='communityalerts/', blank=True, null=True)
    hashtags = ArrayField(models.CharField(
        max_length=225, blank=True, null=True), blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    upvote_count = models.PositiveIntegerField(default=0)
    downvote_count = models.PositiveIntegerField(default=0)
    is_reported = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    flagged_by = models.ManyToManyField(
        get_user_model(), blank=True, related_name='flaggers')
    reported_by = models.ManyToManyField(
        get_user_model(), blank=True, related_name='reporters')
    upvoted_by = models.ManyToManyField(
        get_user_model(), blank=True, related_name='upvoters')
    downvoted_by = models.ManyToManyField(
        get_user_model(), blank=True, related_name='downvoters')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.first_name + ' ' + self.author.last_name
