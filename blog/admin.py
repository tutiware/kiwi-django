from django.contrib import admin
from blog.models import articleModel, categoryModel, commentModel

admin.site.register(categoryModel)


class articlesAdmin(admin.ModelAdmin): #panel uzerindeki ozelliklerini bu sinif ile belirliyoruz
    search_fields = ('title', 'content') #
    list_display = ('title', 'author', 'first_published', 'last_edited')

admin.site.register(
    articleModel,
    articlesAdmin,  #üstte yazılan sınıfı registerin içine yazılan modelle eşler ve panele tanıtır
)

class commentAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content',)
    list_display = ('article', 'author', 'title', 'first_published', 'last_edited') #f

admin.site.register(
    commentModel,
    commentAdmin,
)
