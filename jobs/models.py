from django.db import models


class Job(models.Model):
    company = models.CharField(max_length=255)
    description = models.TextField()
    jobTitle = models.CharField(max_length=255)
    hours = models.IntegerField()
    rate = models.FloatField()
    imgUrl = models.CharField(max_length=255, default="//placehold.it/200X200/")

    def __str__(self):
        return self.company + " " + self.jobTitle
