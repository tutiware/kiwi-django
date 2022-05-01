from django.db import models
from autoslug import AutoSlugField

class categoryModel(models.Model):
    title = models.CharField( #defines a name made of characters
        max_length = 30, #limits char length of title
        blank = False, #sets whether you'are letting the name to be " "
        null = False #sets whether you'are letting the name undefined
        )
    slug = AutoSlugField( #defines URL of the category like site.com/category/catg_1
        populate_from ='title', #sets title of the category as URL like category/<title>
        unique = True #in case of conflict with existed URL, it generates a new unique one
    )

    class Meta: #meta class lets you set additional specialized options into your model
        db_table = 'category' #sets the table name
        verbose_name = 'category' #specifies the name of your model on panel.
        verbose_name_plural = 'categories' #for the case plural examples take place

    def __str__(self):
        return self.title #nesne panel tarafindan bu isimle taninir