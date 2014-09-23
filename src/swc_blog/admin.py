from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from .models import Post


class PostAdmin(MarkdownModelAdmin):
    list_display = ("pub_date", "title", "mod_date", "status")
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Post, PostAdmin)