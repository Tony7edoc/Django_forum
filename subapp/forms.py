from dataclasses import fields
from django import forms

from pyexpat import model
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
