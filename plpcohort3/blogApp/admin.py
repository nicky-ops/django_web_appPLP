from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = (
        'title', 'content', 'date', 'author'
    )
    list_filter = (
        'author', 'date'
    )
    list_max_show_all = 1