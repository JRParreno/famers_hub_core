# Generated by Django 4.1.1 on 2022-09-18 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0003_alter_season_season_image'),
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendationseasons',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendation_season', to='season.season'),
        ),
    ]
