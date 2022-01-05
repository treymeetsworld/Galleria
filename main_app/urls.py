from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('galleries/', views.galleries_index, name='galleries_index'),
  path('galleries/personal', views.personal_index, name='personal_index'),
  path('galleries/<int:gallery_id>/', views.galleries_detail, name='galleries_detail'),
  path('galleries/create/', views.GalleryCreate.as_view(), name='galleries_create'),
  path('galleries/<int:pk>/update/', views.GalleryUpdate.as_view(), name='galleries_update'),
path('galleries/<int:pk>/delete/', views.GalleryDelete.as_view(), name='galleries_delete'),
path('galleries/<int:gallery_id>/add_comment/', views.add_comment, name='add_comment'),
path('artwork/create/', views.ArtworkCreate.as_view(), name='artwork_create'),
path('artwork/<int:pk>/', views.ArtworkDetail.as_view(), name='artwork_detail'),
  path('artwork/', views.ArtworkList.as_view(), name='artwork_index'),
  path('artwork/<int:pk>/update/', views.ArtworkUpdate.as_view(), name='artwork_update'),
  path('artwork/<int:pk>/delete/', views.ArtworkDelete.as_view(), name='artwork_delete'),
  path('galleries/<int:gallery_id>/assoc_artwork/<int:artwork_id>/', views.assoc_artwork, name='assoc_artwork'),
  path('galleries/<int:gallery_id>/assoc_art/<int:art_id>/', views.assoc_art, name='assoc_art'),
  path('galleries/<int:gallery_id>/add_photo/', views.add_photo, name='add_photo'),
  path('api/', views.search, name='search'),
  path('api/search', views.searchRequest, name='search-request'),
  path('api/artwork/', views.art_index, name='art-index'),
path('api/artwork/<int:pk>/', views.art_detail, name='art_detail')  
]