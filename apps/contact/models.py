from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    quilt_id = models.IntegerField()
    quilt_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    user_name = models.CharField(max_length=100)
    owner_id = models.IntegerField(default=0,blank=True)
    date_added = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
