# Generated by Django 4.1.1 on 2022-10-15 21:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fscohort', '0002_remove_postviews_time_stamp_alter_like_created_by_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostViews',
            new_name='PostView',
        ),
    ]