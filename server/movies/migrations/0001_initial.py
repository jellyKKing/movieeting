# Generated by Django 3.2.6 on 2022-11-24 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('youtube', models.CharField(blank=True, max_length=128, null=True)),
                ('vote_count', models.IntegerField()),
                ('actors', models.ManyToManyField(related_name='movie_actors', to='movies.Actor')),
                ('directors', models.ManyToManyField(related_name='movie_directors', to='movies.Director')),
                ('genres', models.ManyToManyField(related_name='movie_genres', to='movies.Genre')),
                ('keywords', models.ManyToManyField(related_name='movie_keywords', to='movies.Keyword')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_survey', models.IntegerField(default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
