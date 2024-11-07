from django.db import models



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    role = models.CharField(max_length=255)
    date_of_registration = models.DateTimeField(auto_now_add=True)
    # avatar
    # projects = Task(models.Model)

    def __str__(self):
        return self.email