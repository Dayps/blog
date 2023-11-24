from django.contrib import admin
from .models import Posts
from .models import Comment
from .models import Category

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Posts)
