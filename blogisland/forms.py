"""Imports"""
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Form for adding comments to the blogs"""
    class Meta:
        """Meta Class"""
        model = Comment
        fields = ('body',)
