from django.shortcuts import render, redirect
from django.http import HttpResponse
import youtube_dl
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')



def download_video(request):
    if request.method == 'POST':
        video_url = request.POST['url']
        if video_url:
            ydl_opts = {'outtmp1': 'D:/'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            messages.success(request, 'Video Downloaded.')
            return redirect('home')
        else:
            messages.warning(request, 'Please Enter Video URL')
            return redirect('home')
    return redirect('home')