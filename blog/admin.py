from django.contrib import admin
from blog.models import article, categoryModel

admin.site.register(categoryModel)
admin.site.register(articleModel)