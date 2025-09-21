from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at"]
    list_filter = ["created_at", "author"]
    search_fields = ["title", "content"]


admin.site.register(Post, PostAdmin)
