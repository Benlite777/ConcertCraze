# Generated by Django 4.2.7 on 2024-02-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0024_artist_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="artist",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="artist_images"),
        ),
    ]
