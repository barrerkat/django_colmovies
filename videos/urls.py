from django.urls import path

from . import views

app_name = 'videos'

urlpatterns = [
    path('<slug>/', views.video_detail, name='detail'),
]
