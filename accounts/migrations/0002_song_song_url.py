# Generated by Django 4.2.7 on 2024-02-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="song_url",
            field=models.URLField(
                default="https://youtu.be/RGBeJad8VrE?si=RR5uk3cEcbucd8OZ"
            ),
        ),
    ]
