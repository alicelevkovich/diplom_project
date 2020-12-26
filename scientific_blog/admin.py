from django.contrib import admin
from scientific_blog.models import User, Post, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'password', 'lab')
    fields = ('user_name', 'email', 'password', 'lab')
    list_filter = ('user_name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

