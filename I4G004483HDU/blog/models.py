from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    published_date = models.DateTimeField()
    created_date = models.DateTimeField()
    text = models.TextField()
