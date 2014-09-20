from django.contrib import admin
from swc_blog.models import Post
from django_markdown.admin import MarkdownModelAdmin


class PostAdmin(MarkdownModelAdmin):
    list_display = ("pub_date", "title", "mod_date", "status")
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Post, PostAdmin)