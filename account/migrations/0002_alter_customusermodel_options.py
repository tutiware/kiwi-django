# Generated by Django 3.2 on 2022-04-11 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customusermodel',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
