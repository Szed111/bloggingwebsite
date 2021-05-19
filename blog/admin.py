from django.contrib import admin
from .models import Post, Comment, ImpLink

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ImpLink)