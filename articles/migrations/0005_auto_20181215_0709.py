# Generated by Django 2.1.2 on 2018-12-15 07:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ForeignKey(default=None, on_delete=True, to='articles.Comment'),
        ),
    ]