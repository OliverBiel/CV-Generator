from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    logo = models.TextField(max_length=100)
    info = models.CharField(max_length=100)

    def __str__(self):
        return self.name
