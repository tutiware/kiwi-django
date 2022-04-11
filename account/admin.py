from django.contrib import admin
from account.models import CustomUserModel
from django.contrib.auth.admin import UserAdmin

class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ('username', 'email')

admin.site.register(CustomUserModel, CustomAdmin)