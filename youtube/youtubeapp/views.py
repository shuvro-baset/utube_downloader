from django.shortcuts import render, redirect
# pytub package for download youtube video
from pytube import YouTube
import os
from django.http import FileResponse
import pafy


def ytb_down(request):
    if request.method == 'POST':
        url = request.POST.get('ylink')
        video = pafy.new(url)
        embedlink = url.replace("watch?v=", "embed/")
        context = {
            'yobj': video,
            'embedlink': embedlink,
        }
        return render(request, 'ytb_main.html', context)
    return render(request, 'ytb_main.html')
