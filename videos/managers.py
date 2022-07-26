from django.db import models

from .models import Video


class PublicVideoManager(models.Manager):
    """A manager for the Video model."""

    def public(self, **kwargs):
        """Return only videos that has been set to Public."""
        return self.filter(privacy=Video.PUBLIC, **kwargs)
