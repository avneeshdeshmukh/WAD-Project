# Generated by Django 5.0 on 2024-04-12 13:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourApp', '0007_restaurant_pricerange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantimage',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_images', to='TourApp.restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurantreview',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_review', to='TourApp.restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurantreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TouristPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100000)),
                ('mapLocation', models.TextField(max_length=100000)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('description', models.TextField(max_length=1000000)),
                ('entryFees', models.IntegerField(default=0)),
                ('categories', models.ManyToManyField(to='TourApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='TouristPlaceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tourist_place_images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tourist_place_images', to='TourApp.touristplace')),
            ],
        ),
        migrations.CreateModel(
            name='TouristPlaceReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('comment', models.TextField(max_length=1000000)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tourist_place_review', to='TourApp.touristplace')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
