from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gallery
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
  return render(request, 'galleries/detail.html', { 'gallery': gallery })

class GalleryCreate(CreateView):
  model = Gallery
  fields = '__all__'
  
class GalleryUpdate(UpdateView):
  model = Gallery
  fields = ['description', 'artwork', 'comments']

class GalleryDelete(DeleteView):
  model = Gallery
  success_url = '/galleries/'