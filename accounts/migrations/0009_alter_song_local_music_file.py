# Generated by Django 4.2.7 on 2024-02-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_song_local_music_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="local_music_file",
            field=models.FileField(
                default="01_-_Chris_Tomlin_-_Indescribable.mp3", upload_to="songs/"
            ),
        ),
    ]
