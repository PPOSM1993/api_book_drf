# Generated by Django 5.0.6 on 2024-05-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=3, max_length=150),
            preserve_default=False,
        ),
    ]
