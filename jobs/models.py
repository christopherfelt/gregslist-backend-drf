from django.db import models


class Job(models.Model):
    company = models.CharField(max_length=255)
    description = models.TextField()
    jobTitle = models.CharField(max_length=255)
    hours = models.IntegerField()
    rate = models.FloatField()

    def __str__(self):
        return self.company + " " + self.jobTitle
