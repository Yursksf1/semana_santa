from django.shortcuts import render
from myapp.models import Video
# Create your views here.

def ver_videos(request):
    videos =  Video.objects.all()
    context = {
        "videos": videos,
    }
    return render(request, "myapp/videos.html", context)