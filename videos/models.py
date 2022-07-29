from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Genre(models.Model):
    """Genre model"""
    
    name = models.CharField(verbose_name=_('name'),
                            max_length=150,
                            db_index=True,
                            help_text=_('Genre name.'),
                            unique=True)
    slug = models.SlugField(verbose_name=_('slug'),
                            max_length=100,
                            unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('genre')
        verbose_name_plural = _('genres')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={'slug': self.slug})


class Video(models.Model):
    """Video model"""
    
    PRIVATE = 'PR'
    PUBLIC = 'PU'
    PRIVACY_CHOICES = [
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public'),
    ]

    GENERAL = 'G'
    PARENTAL = 'PG'
    MATURED = 'M'
    RATING_CHOICES = [
        (GENERAL, 'General Audience'),
        (PARENTAL, 'Parental Guidance Suggested'),
        (MATURED, 'Mature Audience Only'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name=_('videos'),
                             verbose_name=_('user'))
    title = models.CharField(verbose_name=_('title'),
                             max_length=250,
                             db_index=True,
                             help_text=_('Title of the video.'))
    slug = models.SlugField(verbose_name=_('slug'),
                            max_length=100,
                            unique=True)
    video_file = models.FileField(verbose_name=_('Video file'),
                                  upload_to='videos',
                                  help_text=_('Path to the uploaded video.'))
    # ToDo: Autogenerate thumbnail
    thumbnail = models.ImageField(verbose_name=_('thumbnail'),
                                  upload_to='thumbnails',
                                  help_text=_('An image that will be used as a thumbnail.'))
    description = models.TextField(verbose_name=_('description'),
                                   max_length=1000,
                                   help_text=_('Description of the video.'))
    privacy = models.CharField(verbose_name=_('privacy'),
                               max_length=2,
                               choices=PRIVACY_CHOICES,
                               default=PUBLIC)
    movie_rating = models.CharField(verbose_name=_('movie rating'),
                                    max_length=2,
                                    choices=RATING_CHOICES)
    impressions = models.PositiveBigIntegerField(verbose_name=_('impressions'),
                                                 default=0,
                                                 help_text=_('View count for a video.'))
    genre = models.ForeignKey(Genre,
                              on_delete=models.PROTECT,
                              related_name=_('videos'),
                              verbose_name=_('genre'),
                              blank=True)
    released = models.DateField(blank=True, null=True)
    enable_comments = models.BooleanField(verbose_name=_('enable comments'),
                                          default=True,
                                          help_text=_('Flag to turn on/off commenting'))
    # enable_downloads
    created = models.DateTimeField(verbose_name=_('created'),
                                   auto_now_add=True,
                                   help_text=_('The date/time when the user uploaded the video'))
    updated = models.DateTimeField(verbose_name=_('updated'),
                                   auto_now=True,
                                   help_text=_('The date/time when the user made changes to the video information'))
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name=_('favorites'),
                                       verbose_name=_('user favorites'),
                                       blank=True,
                                       null=True,
                                       help_text=_('Users who added video to their favorites.'))
    # video_length
    # tags
    # flag(ged)

    class Meta:
        ordering = ['-created']
        verbose_name = _('video')
        verbose_name_plural = _('videos')

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={'slug': self.slug})
