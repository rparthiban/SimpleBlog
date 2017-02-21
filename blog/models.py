from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone

CATEGORIES = [
    ('PUB', 'Public'),
    ('POL', 'Politics'),
    ('SCI', 'Science'),
    ('TEC', 'Technolgy'),
    ('OTH', 'Others'),
]

# Create your models here.
class Blog(models.Model):
    """Blog Schema defined here."""

    title = models.CharField("Title", max_length=100, unique=True, blank=False)
    user = models.CharField("User", max_length=32, blank=False)
    category = models.CharField("Category", max_length=3, choices=CATEGORIES, default='OTH')
    content = models.TextField("Content", blank=True)
    posted = models.DateField(db_index=True, auto_now_add=True)
    accepted = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['-posted']

    def was_posted_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.posted <= now
