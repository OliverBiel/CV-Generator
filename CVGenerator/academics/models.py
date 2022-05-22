from django.db import models


class Academic(models.Model):
    name = models.CharField(max_length=60)
    institution = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('start_date',)