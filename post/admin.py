from django import forms
from django.contrib import admin
from .models import Post, Like, Bookmark

# Register your models here.
class PostForm(forms.ModelForm) :
    content = forms.CharField(widget=forms.Textarea)

    class Meta :
        model = Post
        fields = '__all__'

class LikeInLine(admin.TabularInline) :
    model=Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin) :
    list_display = ['id', 'author', 'nickname', 'content', 'created_at']
    list_display_links = ['author', 'nickname', 'content']

    def nickname(request, post) :
        return post.author.profile.nickname

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin) :
    list_display = ['id', 'post', 'user', 'created_at']     # 보여주는 부분
    list_istplay_links = ['post', 'user']       # 링크가 달리는 부분

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin) :
    list_display = ['id', 'post', 'user', 'created_at']
    list_display_links = ['post', 'user']
