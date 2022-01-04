from django.forms import ModelForm, TextInput
from .models import Comment, Art

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']
    

class ArtForm(ModelForm):
  class Meta:
    model = Art
    fields = '__all__'
    widgets = { '' : TextInput(attrs={'placeholder' : 'Search', 'class' : 'input'})}