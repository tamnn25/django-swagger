# Generated by Django 4.2 on 2023-04-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_article_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date_time',
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
