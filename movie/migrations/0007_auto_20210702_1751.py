# Generated by Django 3.2.4 on 2021-07-02 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20210702_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(blank=True, to='movie.Categories'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
