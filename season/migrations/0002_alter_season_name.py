# Generated by Django 4.1.1 on 2022-09-18 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='name',
            field=models.CharField(choices=[('DRY', 'Dry Season'), ('WET', 'Wet Season'), ('N/A', 'N/A')], default='N/A', max_length=100),
        ),
    ]
