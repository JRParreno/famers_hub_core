# Generated by Django 4.1.1 on 2022-09-18 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0003_alter_season_season_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/seasons/'),
        ),
    ]
