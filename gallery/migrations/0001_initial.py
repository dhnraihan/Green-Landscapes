# Generated by Django 5.2.1 on 2025-05-30 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=120, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery Categories',
            },
        ),
        migrations.CreateModel(
            name='BeforeAfterImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('before_image', models.ImageField(upload_to='before_after/before/')),
                ('after_image', models.ImageField(upload_to='before_after/after/')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='before_after_images', to='gallery.gallerycategory')),
            ],
            options={
                'verbose_name_plural': 'Before/After Images',
                'ordering': ['-completion_date', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_items', to='gallery.gallerycategory')),
            ],
            options={
                'ordering': ['-completion_date', '-created_at'],
            },
        ),
    ]
