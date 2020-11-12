from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    # description = models.TextField()
    audio_description = models.FileField(upload_to='blog/audio/', null=True)
    image = models.ImageField(upload_to='blog/images/')
    date = models.DateField()

    def __str__(self):
        return self.title