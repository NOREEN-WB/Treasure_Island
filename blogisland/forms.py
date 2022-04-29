"""Imports"""
from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    """to create post"""
    class Meta:
        """Meta Class"""
        model = Post
        fields = (
            'title',
            'slug',
            'author',
            'featured_image',
            'content',
            'status'
        )

        # choices=choice_list,
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }



class CommentForm(forms.ModelForm):
    """Form for adding comments to the blogs"""
    class Meta:
        """Meta Class"""
        model = Comment
        fields = ('body',)
