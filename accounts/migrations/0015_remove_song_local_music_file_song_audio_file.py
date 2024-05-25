# Generated by Django 4.2.7 on 2024-02-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0014_alter_song_local_music_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="song",
            name="local_music_file",
        ),
        migrations.AddField(
            model_name="song",
            name="audio_file",
            field=models.FileField(
                default="STHUTHIGE_YOGYANU_OFFICIAL_KANNADA_WORSHIP_SONG_MAHIMEYA_ARASANU_PAS.SIMON_MOSES.mp3",
                upload_to="songs/",
            ),
        ),
    ]
