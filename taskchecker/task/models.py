from django.db import models



class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # project = models.CharField(max_length=255)
    # contractor = models.CharField(max_length=255)
    # status = models.CharField(max_length=255)
    # priority = models.CharField(max_length=255)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)
    # due_date = models.DateTimeField()
    # responsible_for_testing = models.CharField(max_length=255)

    # comments = models.