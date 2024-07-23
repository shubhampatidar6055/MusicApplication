from django.db import models

# Create your models here.
class Song(models.Model):
    song_name = models.CharField(max_length=250)
    song = models.FileField(upload_to='songs')

    def __str__(self):
        return str(self.name)
    
