# Generated by Django 5.1.6 on 2025-03-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Rated', models.CharField(max_length=10)),
                ('Released', models.CharField(max_length=20)),
                ('Genre', models.CharField(max_length=50)),
                ('Director', models.CharField(max_length=50)),
                ('Actors', models.CharField(max_length=200)),
                ('Writer', models.CharField(max_length=200)),
                ('Plot', models.CharField(max_length=500)),
                ('Awards', models.CharField(max_length=200)),
                ('Poster', models.CharField(max_length=200)),
                ('imdbRating', models.CharField(max_length=5)),
                ('Type', models.CharField(max_length=20)),
            ],
        ),
    ]
