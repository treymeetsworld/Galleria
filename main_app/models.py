from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Artwork(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  artist = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  year =  models.IntegerField()
  
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('artwork_detail', kwargs={'pk': self.id})
  
  
class Gallery(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  artwork = models.ManyToManyField(Artwork)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('galleries_detail', kwargs={'gallery_id': self.id})
  
class Photo(models.Model):
  url = models.CharField(max_length=250)
  gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for gallery_id: {self.gallery_id} @{self.url}"
  
class Comment(models.Model):
  comment = models.TextField('', max_length=250)
  gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.comment
  
class Search(models.Model):
  q = models.CharField(max_length=50)
  
  def __str__(self):
    return self.q