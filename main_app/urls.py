from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('galleries/', views.galleries_index, name='galleries_index'),
  path('galleries/<int:gallery_id>/', views.galleries_detail, name='galleries_detail'),
  path('galleries/create/', views.GalleryCreate.as_view(), name='galleries_create'),
  path('galleries/<int:pk>/update/', views.GalleryUpdate.as_view(), name='galleries_update'),
path('galleries/<int:pk>/delete/', views.GalleryDelete.as_view(), name='galleries_delete'),
]