# Generated by Django 4.2.7 on 2024-02-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_song_song_url_song_local_file_path"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="song",
            name="local_file_path",
        ),
        migrations.AddField(
            model_name="song",
            name="local_music_file",
            field=models.FileField(default="", upload_to="accounts/media/song"),
        ),
    ]
