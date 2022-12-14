# Generated by Django 4.1 on 2022-09-18 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agriculture', '0002_agriculturetype'),
        ('recommendation', '0006_alter_recommendationseasons_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='agriculture_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agriculture_type', to='agriculture.agriculturetype'),
        ),
    ]
