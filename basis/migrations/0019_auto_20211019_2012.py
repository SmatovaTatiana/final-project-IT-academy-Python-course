# Generated by Django 3.2.8 on 2021-10-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basis', '0018_topnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='topnews',
            name='slug',
            field=models.SlugField(default='', max_length=300, unique='project_name'),
        ),
        migrations.AlterField(
            model_name='topnews',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
