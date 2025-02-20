# Generated by Django 5.1.2 on 2024-12-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('day', models.DateTimeField(auto_now_add=True)),
                ('like', models.FloatField()),
                ('comments', models.IntegerField()),
            ],
        ),
    ]
