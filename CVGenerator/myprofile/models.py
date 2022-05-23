from django.db import models


class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo')
    description = models.TextField()

    def __str__(self):
        return self.name
