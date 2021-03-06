from django.db import models
from autoslug import AutoSlugField
from blog.models.category import categoryModel
from ckeditor.fields import RichTextField


class articleModel(models.Model):
    cover = models.ImageField(
        upload_to="article_covers"
    )  # "pipenv install Pillow" needed for ImageField function
    title = models.CharField(
        max_length=50,
        blank = False,
        null = False)
    categories = models.ManyToManyField(  # kategori başlığı altında iki küme arasında çoklu eşleşmeyi sağlar
        categoryModel,  # eşleşeceği küme
        related_name="articles",  # bu modelin örnekleri de eşleştirmede articles olarak etiketlendi
    )
    author = models.ForeignKey(
        'account.CustomUserModel',  # üyeler tablosuyla eşleştirir
        related_name="articles",  # bu modelin örnekleri de eşleştirmede articles olarak etiketlendi
        on_delete=models.CASCADE,  # bu eşleştirmede bir author silinirse onunla bağlantılı objeler de silinir
    )   
    content = RichTextField(default = 'blank')
    first_published = models.DateTimeField(
        auto_now_add=True
    )  # sets the time when the article added
    last_edited = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from="title", unique=True)

    class Meta:
        db_table = "article"
        verbose_name = "article"
        verbose_name_plural = "articles"

    def __str__(self):
        return self.title
