from django.contrib import admin
from blog.models import articleModel, categoryModel

admin.site.register(categoryModel)
class articlesAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'first_published', 'last_edited'
    )
admin.site.register(articleModel, articlesAdmin)
