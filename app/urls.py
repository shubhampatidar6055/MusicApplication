from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", category),
    path("addsong/", addsong),
    path("song/", song),
    path("delete_song/<int:pk>/", delete_song, name="delete_song"),
    path("update_song/<int:uid>/",update_song, name="update_song"),
    path("update_song_data/", update_song_data),
    path("download_song/<int:pk>/", download_song, name="download_song")
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
