# Generated by Django 5.0.6 on 2024-05-13 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
    ]
