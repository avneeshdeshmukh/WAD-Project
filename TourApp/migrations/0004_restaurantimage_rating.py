# Generated by Django 5.0 on 2024-04-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TourApp', '0003_category_alter_restaurantimage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantimage',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]