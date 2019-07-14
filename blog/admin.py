from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text')
    list_display = ('title', 'published',)
    list_display_links = ('title',)
