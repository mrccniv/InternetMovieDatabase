# Generated by Django 3.2.4 on 2021-06-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='photo',
            field=models.ImageField(default='defaultImg.png', upload_to='movie'),
        ),
    ]
