from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Gallery(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  artwork = models.CharField(max_length=100)
  comments = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('galleries_detail', kwargs={'gallery_id': self.id})
  
class Artwork(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  artist = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  year =  models.IntegerField()
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('artwork_detail', kwargs={'pk': self.id})