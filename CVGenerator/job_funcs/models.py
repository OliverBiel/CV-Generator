from django.db import models


class JobFunc(models.Model):
    func = models.CharField(max_length=75)

    def __str__(self):
        return self.func