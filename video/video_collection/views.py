from django.shortcuts import render
from .models import Video
from .forms import VideoForm

def home(request):
    app_name = 'Video List'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

def add(request):
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form' : new_video_form})