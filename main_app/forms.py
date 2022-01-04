from django.forms import ModelForm, TextInput
from .models import Comment, Search

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']
    

class SearchForm(ModelForm):
  class Meta:
    model = Search
    fields = ['q']
    widgets = { 'q' : TextInput(attrs={'placeholder' : 'Search', 'class' : 'input'})}