from django.db import models
# O modelo Post tem um título, conteúdo e data de postagem
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)