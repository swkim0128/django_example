from django import forms
from django.contrib import admin
from .models import Post

# Register your models here.
class PostForm(forms.ModelForm) :
    content = forms.CharField(widget=forms.Textarea)

    class Meta :
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin) :
    list_display = ['id', 'author', 'nickname', 'content', 'created_at']
    list_display_links = ['author', 'nickname', 'content']

    def nickname(request, post) :
        return post.author.profile.nickname