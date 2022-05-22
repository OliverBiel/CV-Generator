from django.db import models
from job_funcs.models import JobFunc


class Experience(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    job_func = models.ManyToManyField(JobFunc)

    def __str__(self):
        return self.company
    
    class Meta:
        ordering = ('start_date',)