# Generated by Django 4.2.7 on 2024-02-11 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_alter_song_local_music_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="local_music_file",
            field=models.FileField(
                default="mywebsite/accounts/media/08 - Better Is One Day.mp3",
                upload_to="media/",
            ),
        ),
    ]
