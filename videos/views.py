from django.shortcuts import get_object_or_404, render

from .models import Video


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
