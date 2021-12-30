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
path('artwork/create/', views.ArtworkCreate.as_view(), name='artwork_create'),
path('artwork/<int:pk>/', views.ArtworkDetail.as_view(), name='artwork_detail'),
  path('artwork/', views.ArtworkList.as_view(), name='artwork_index'),
  path('artwork/<int:pk>/update/', views.ArtworkUpdate.as_view(), name='artwork_update'),
  path('artwork/<int:pk>/delete/', views.ArtworkDelete.as_view(), name='artwork_delete'),
  path('galleries/<int:gallery_id>/assoc_artwork/<int:artwork_id>/', views.assoc_artwork, name='assoc_artwork'),
  path('galleries/<int:gallery_id>/add_photo/', views.add_photo, name='add_photo'),
  
]