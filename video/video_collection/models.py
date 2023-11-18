from django.db import models

class Video(models.Model):
    name = models.TextField(max_length=200)
    url = models.TextField(max_length=400)
    notes = models.TextField(blank=True, null=True)
    video_id = models.CharField(max_length=40, unique=True, default='None')

    def __str__(self):
        
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Notes: {self.notes[:200]}'