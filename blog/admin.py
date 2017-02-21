from django.contrib import admin

# Register your models here.
from models import Blog


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'user']}),
        ('Information', {'fields': ['category', 'content', 'accepted']}),
    ]
    list_display = ('title', 'category', 'user', 'accepted', 'posted')
    list_filter = ['title', 'category', 'user']
    search_fields = ['title', 'user']

admin.site.register(Blog, BlogAdmin)
