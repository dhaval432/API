
from django import forms
from .models import Blog, Comment

class Blog_form(forms.Modelform):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

class Comment_form(forms.Modelform):
    class Meta:
        model = Comment
        fields = ['text']

