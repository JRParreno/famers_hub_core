# Generated by Django 4.1 on 2022-09-19 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0009_recommendation_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='name',
            new_name='title',
        ),
    ]
