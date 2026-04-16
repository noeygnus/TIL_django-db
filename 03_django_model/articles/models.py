from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=10) 
    content = models.TextField() #길이 제한이 없음 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
