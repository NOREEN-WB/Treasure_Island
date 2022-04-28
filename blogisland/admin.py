from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """PostAdmin class"""
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """CommentAdmin Class"""
    list_display = ['name', 'body', 'post', 'created_on']
    list_filter = ['created_on']
    search_fields = ['name', 'email', 'body']
