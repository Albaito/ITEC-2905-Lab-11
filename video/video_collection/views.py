from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.contrib import messages

def home(request):
    app_name = 'Video List'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

def add(request):
    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            new_video_form.save()
            messages.info(request, 'New video saved!')
            # TODO: redirect to a list of videos
        else:
            messages.warning(request, 'Check the data entered!')
            return render(request, 'video_collection/add.html', {'new_video_form' : new_video_form})
        
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

def video_list(request):
    videos = Video.objects.get.order_by('name')
    return render(request, 'video_collection/video_list.html', {'videos': videos})