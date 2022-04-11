from django.contrib import admin
from blog.models import articleModel, categoryModel, commentModel

admin.site.register(categoryModel)
admin.site.register(commentModel)

class articlesAdmin(admin.ModelAdmin):
    search_fields = ("title", "author")
    list_display = ("title", "first_published", "last_edited")


admin.site.register(
    articleModel,
    articlesAdmin,  # üstte yazılan sınıfı registerin içine yazılan modelle eşler ve panele tanıtır
)
