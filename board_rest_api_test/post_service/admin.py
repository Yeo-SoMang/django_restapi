from django.contrib import admin

from post_service.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','regdate',)

admin.site.register(Post, PostAdmin)