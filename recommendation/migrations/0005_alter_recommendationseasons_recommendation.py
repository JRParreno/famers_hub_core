# Generated by Django 4.1.1 on 2022-09-18 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_remove_recommendation_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendationseasons',
            name='recommendation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendation_season', to='recommendation.recommendation'),
        ),
    ]
