from urllib import parse
from django.db import models
from django.core.exceptions import ValidationError


class Video(models.Model):
    name = models.TextField(max_length=200)
    url = models.TextField(max_length=400)
    notes = models.TextField(blank=True, null=True)
    video_id = models.CharField(max_length=40, unique=True, default='None')


    def save(self, *args, **kwargs):
        try:
            # Checks if the url doesn't use HTTPS, isn't from youtube.com, or doesn't includes a youtube video link
            url_components = parse.urlparse(self.url)
            if url_components.scheme != 'https' or url_components.netloc != 'www.youtube.com' or url_components.path != '/watch':
                raise ValidationError(f'Invalid Youtube URL {self.url}')    
            
            query_string = url_components.query
            if not query_string:
                raise ValidationError(f'Invalid Youtube URL {self.url}')

            parameters = parse.parse_qs(query_string, strict_parsing=True)
            parameters_list = parameters.get('v')
            if not parameters_list:
                raise ValidationError(f'Invalid Youtube URL parameters {self.url}')
            
            self.video_id = parameters_list[0]
        
        except ValueError as e:
            raise ValidationError(f'Unable to') from e
        
        super().save(*args, **kwargs)

    def __str__(self):
        
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Notes: {self.notes[:200]}, Video ID: {self.video_id}'