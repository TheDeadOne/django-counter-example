from django.contrib import admin

from .models import PageHit

@admin.register(PageHit)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('url', 'count',)
    list_display = ('url', 'count',)
    list_display_links = ('url',)

    def has_add_permission(self, request):
        return False
