from django.contrib import admin
from .models import Gallery, Comment, Artwork, Photo, Art
# Register your models here.
admin.site.register(Gallery)
admin.site.register(Comment)
admin.site.register(Artwork)
admin.site.register(Photo)
admin.site.register(Art)