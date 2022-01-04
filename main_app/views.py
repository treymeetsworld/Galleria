from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Gallery, Artwork, Photo, Search
from .forms import CommentForm, SearchForm
import uuid
import boto3
import requests

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'galleria-artwork'
# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)



def galleries_index(request):
  galleries = Gallery.objects.all()
  return render(request, 'galleries/index.html', { 'galleries': galleries })

def personal_index(request):
  galleries = Gallery.objects.filter(user=request.user)
  return render(request, 'galleries/personal.html', { 'galleries': galleries })

@login_required(login_url='/')
def galleries_detail(request, gallery_id):
  gallery = Gallery.objects.get(id=gallery_id)
  comment_form = CommentForm()
  artwork_gallery_doesnt_have = Artwork.objects.exclude(id__in = gallery.artwork.all().values_list('id'))
  return render(request, 'galleries/detail.html', { 'gallery': gallery,'comment_form': comment_form,  'artwork': artwork_gallery_doesnt_have })

class GalleryCreate(LoginRequiredMixin,CreateView):
  model = Gallery
  fields = ['name', 'description', ]
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
def add_comment(request, gallery_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.gallery_id = gallery_id
    new_comment.save()
  return redirect('galleries_detail', gallery_id=gallery_id)
  
class GalleryUpdate(LoginRequiredMixin,UpdateView):
  model = Gallery
  fields = ['description', 'artwork', 'comments']

class GalleryDelete(LoginRequiredMixin,DeleteView):
  model = Gallery
  success_url = '/galleries/'
  
class ArtworkCreate(LoginRequiredMixin,CreateView):
  model = Artwork
  fields = '__all__'
  
class ArtworkList(LoginRequiredMixin,ListView):
  model = Artwork

class ArtworkDetail(LoginRequiredMixin,DetailView):
  model = Artwork
  
class ArtworkUpdate(LoginRequiredMixin,UpdateView):
  model = Artwork
  fields = '__all__'

class ArtworkDelete(LoginRequiredMixin,DeleteView):
  model = Artwork
  success_url = '/artwork/'

@login_required(login_url='/')
def assoc_artwork(request, gallery_id, artwork_id):
  Gallery.objects.get(id=gallery_id).artwork.add(artwork_id)
  return redirect('galleries_detail', gallery_id=gallery_id)

@login_required(login_url='/')
def add_photo(request, gallery_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, gallery_id=gallery_id)
      gallery_photo = Photo.objects.filter(gallery_id=gallery_id)
      if gallery_photo.first():
        gallery_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('galleries_detail', gallery_id=gallery_id)


# def add_artwork(request):
#   url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&isHighlight=true&q={}\ '
  
#   if request.method == 'POST':
#     form = ArtForm(request.POST)
#     form.save()
  
#   form = ArtForm()
  
#   queries = Art.objects.all()
  
#   list_data = []
  
#   for art in queries:
#     r = requests.get(url.format(art)).json()
#     search_id = r['objectIDs'][0]
    
  
#     details = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{search_id}'
#     x = requests.get(details).json()
    
#     art_data = {
#       'image' : x['primaryImageSmall'],
#       'name' : x['title'],
#       'artist' : x['artistDisplayName'],
#       'country' : x['culture'],
#       'year' : x['objectEndDate'],
#     }
    
#     list_data.append(art_data)
    
#   context = {'list_data' : list_data, 'form' : form}
#   return render(request, 'api.html', context)


# def search(request):
#   url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true\ '
  
  
#   # if request.method == 'GET':
#   #   form = SearchForm(request.GET)
    
  
#   # form = SearchForm()
  
#   query = 'q'
  
#   list_data = []
  
  
#   r = requests.get(url.format(query)).json()
#   id_list = r['objectIDs'][:10]
  
#   for id in id_list:
#     details = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}'
#     x = requests.get(details).json()
    
#     art_data = {
#       'image' : x['primaryImageSmall'],
#       'title' : x['title'],
#       'artist' : x['artistDisplayName'],
#       'country' : x['culture'],
#       'year' : x['objectEndDate'],
#     }
#     list_data.append(art_data)
  
#   context = {'list_data' : list_data}
  # return render(request, 'api.html', context)


def search(request):

  return render(request, 'api.html', )


def searchRequest(request):
  url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&q={}'
  
  q = request.GET['q']
  
  list_data = []
  
  r = requests.get(url.format(q)).json()
  id_list = r['objectIDs'][:10]
  
  for id in id_list:
    details = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}'
    x = requests.get(details).json()
    
    art_data = {
      'image' : x['primaryImageSmall'],
      'title' : x['title'],
      'artist' : x['artistDisplayName'],
      'country' : x['culture'],
      'year' : x['objectEndDate'],
    }
    list_data.append(art_data)
    
  context = { 'list_data': list_data}
  return render(request, 'api.html', context)

