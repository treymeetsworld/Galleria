from django.forms import ModelForm, TextInput
from .models import Comment, Search

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']
    

class SearchForm(ModelForm):
  class Meta:
    model = Search
    fields = ['title']
    widgets = { 'title' : TextInput(attrs={'placeholder' : 'Search', 'class' : 'input'})}