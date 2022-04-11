from django.db import models
from blog.models import articleModel
from ckeditor.fields import RichTextField

class commentModel(models.Model):
    author = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='yorumlar')
    article = models.ForeignKey(articleModel, on_delete = models.CASCADE, related_name = 'comments')
    content = RichTextField(default = 'blank')
    first_published = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
