# Generated by Django 4.0.6 on 2022-11-19 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_userprofile_profile_photo'),
        ('community', '0002_rename_user_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to='user_profile.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to='user_profile.userprofile'),
            preserve_default=False,
        ),
    ]
