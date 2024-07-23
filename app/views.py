from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.

def category(request):
    song_obj = Song.objects.all()
    return render(request,"category.html",{"song_obj":song_obj})

def addsong(request):
    return render(request, "addsong.html")

def song(request):
    if request.method == "POST":
        song_name = request.POST.get('song_name')
        song = request.FILES.get('song')
        if Song.objects.filter(song=song).exists():
            messages.error(request,"Song Already Exists")
        else:
            Song.objects.create(song_name=song_name,song=song)
            messages.success(request,"Song Added Sucessfully")
            return redirect("/")
        
def delete_song(request,pk):
    Song.objects.get(id=pk).delete()
    return redirect("/")

def update_song(request,uid):
    update_song_obj = Song.objects.get(id=uid)
    return render(request, "update.html", {"update_song_obj":update_song_obj})

def update_song_data(request):
    if request.method == "POST":
        uid = request.POST.get('uid')
        song_name = request.POST.get('song_name')
        song = request.FILES.get('song')
        Song.objects.filter(id=uid).update(song_name=song_name,song=song)
        messages.success(request,"Song Update Sucessfully")
        return redirect("/")

def download_song(request,pk):
    download_obj = Song.objects.get(id=pk)
    response = HttpResponse(song, content_type='audio/mpeg')
    response['Content-Disposition'] = f'attachment; filename="{"song"}.mp3"'
    return response