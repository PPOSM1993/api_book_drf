# Generated by Django 5.0.6 on 2024-05-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=150, verbose_name='Author'),
        ),
    ]