# Generated by Django 5.0.6 on 2024-05-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=150, unique=True, verbose_name='Title Book'),
        ),
    ]
