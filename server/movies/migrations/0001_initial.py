# Generated by Django 3.2.6 on 2022-11-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('profile_path', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('profile_path', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('original_title', models.CharField(max_length=128)),
                ('release_date', models.CharField(max_length=128)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('popularity', models.FloatField()),
                ('overview', models.TextField(blank=True, null=True)),
                ('backdrop_path', models.CharField(max_length=128)),
                ('poster_path', models.CharField(max_length=128)),
                ('vote_average_naver', models.FloatField(blank=True, null=True)),
                ('link_naver', models.TextField(blank=True, null=True)),
                ('actors', models.ManyToManyField(related_name='movie_actors', to='movies.Actor')),
                ('directors', models.ManyToManyField(related_name='movie_directors', to='movies.Director')),
                ('genres', models.ManyToManyField(related_name='movie_genres', to='movies.Genre')),
                ('keywords', models.ManyToManyField(related_name='movie_keywords', to='movies.Keyword')),
            ],
        ),
    ]