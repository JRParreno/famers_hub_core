# Generated by Django 4.1.1 on 2022-09-18 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_alter_recommendationseasons_season'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendationseasons',
            old_name='author',
            new_name='recommendation',
        ),
    ]
