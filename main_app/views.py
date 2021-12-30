from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Gallery, Artwork
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


def galleries_detail(request, gallery_id):
  gallery = Gallery.objects.get(id=gallery_id)
  artwork_gallery_doesnt_have = Artwork.objects.exclude(id__in = gallery.artwork.all().values_list('id'))
  return render(request, 'galleries/detail.html', { 'gallery': gallery, 'artwork': artwork_gallery_doesnt_have })

class GalleryCreate(CreateView):
  model = Gallery
  fields = ['name', 'description', 'comments','user' ]
  
class GalleryUpdate(UpdateView):
  model = Gallery
  fields = ['description', 'artwork', 'comments']

class GalleryDelete(DeleteView):
  model = Gallery
  success_url = '/galleries/'
  
class ArtworkCreate(CreateView):
  model = Artwork
  fields = '__all__'
  
class ArtworkList(ListView):
  model = Artwork

class ArtworkDetail(DetailView):
  model = Artwork
  
class ArtworkUpdate(UpdateView):
  model = Artwork
  fields = '__all__'

class ArtworkDelete(DeleteView):
  model = Artwork
  success_url = '/artwork/'
  
def assoc_artwork(request, gallery_id, artwork_id):
  Gallery.objects.get(id=gallery_id).artwork.add(artwork_id)
  return redirect('galleries_detail', gallery_id=gallery_id)