# Generated by Django 3.2.10 on 2023-03-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]