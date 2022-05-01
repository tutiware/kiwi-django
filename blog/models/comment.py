from django.db import models
from blog.models import articleModel
from ckeditor.fields import RichTextField


class commentModel(models.Model):
    title = models.CharField(
        max_length = 50,
        blank = False,
        null = False)
    author = models.ForeignKey(
        "account.CustomUserModel", #kullanici modeli veritabanina baglanir
        on_delete=models.CASCADE, #bu silinirse tum yorumlar silinir
        related_name="comment" #panelde gorunum
    )
    article = models.ForeignKey(
        articleModel, #yazi modeli veritabanina baglanir
        on_delete=models.CASCADE, #bu silinirse tum yorumlar silinir
        related_name="comments" #panelde gorunum
    )
    content = RichTextField(default="blank") #icerik richtextfeild uygulamasiyla belirlenir
    first_published = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = "comments"

    def __str__(self):
        return (self.title + " at " + self.author.username)