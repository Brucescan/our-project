# Generated by Django 4.2 on 2024-08-05 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_id',
        ),
        migrations.RemoveField(
            model_name='menus',
            name='menu_id',
        ),
        migrations.RemoveField(
            model_name='shops',
            name='shop_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_id',
        ),
    ]
