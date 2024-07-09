from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100, blank=True)
    capacity = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    rsvps = models.ManyToManyField(User, related_name='rsvped_events', blank=True)

    def __str__(self):
        return self.title
class Attendee(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    capacity = models.IntegerField()
    facilities = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


