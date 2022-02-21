from django.db import models

# Create your models here.

from django.utils import timezone

# Create your models here.

from .utils import create_shortened_url

from datetime import datetime, timedelta
import uuid

DEFAULT_EXPIRATION_DAYS = 30

class Shortener(models.Model):

    created = models.DateTimeField(auto_now_add=True) # modified only creation moment

    expire_in = models.DateTimeField(default=datetime.now() + timedelta(days = DEFAULT_EXPIRATION_DAYS))

    # fast test
    #expire_in = models.DateTimeField(default=timezone.now() + timedelta(seconds = DEFAULT_EXPIRATION_DAYS))

    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    name_short_url = models.CharField(max_length=15, unique=True, default=uuid.uuid1)

    class Meta:
        ordering = ["-created"]


    def __str__(self):

        # Description class to show
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):

        if self.name_short_url:
            self.short_url = self.name_short_url

        if not self.short_url:
            self.short_url = create_shortened_url(self)
            self.name_short_url = self.short_url

        super().save(*args, **kwargs)

        self.name_short_url = None

