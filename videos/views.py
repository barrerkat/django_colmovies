from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Video


def index(request):
    videos = Video.objects.filter(privacy='PU')
    context = {'videos': videos}
    return render(request, 'videos/index.html', context)


def video_detail(request, slug):
    """
    Video detail.

    Template: ``videos/video_detail.html``
    Context:
        video
            Given video
    """

    video = get_object_or_404(Video, slug__iexact=slug)

    template = 'videos/video_detail.html'
    context = {
        'video': video,
    }

    return render(request, template, context)

