# Generated by Django 3.2.8 on 2021-10-15 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basis', '0007_alter_uploaddocument_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaddocument',
            name='document',
            field=models.FileField(upload_to='documents/'),
        ),
    ]