# Generated by Django 3.1.6 on 2021-08-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0006_search_data_craeted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search_data',
            name='craeted',
        ),
        migrations.AddField(
            model_name='search_data',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
