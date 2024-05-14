# Generated by Django 5.0.6 on 2024-05-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_book_gender_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genderbooks',
            options={'ordering': ['id'], 'verbose_name': 'Gender Book', 'verbose_name_plural': 'Genders Book'},
        ),
        migrations.AlterField(
            model_name='genderbooks',
            name='name_gender',
            field=models.CharField(max_length=150, unique=True, verbose_name='Gender Book'),
        ),
    ]
