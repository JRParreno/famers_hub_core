# Generated by Django 4.1.1 on 2022-09-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemical_control', '0002_remove_chemicalcontrol_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemicalinstruction',
            name='icon_image',
            field=models.ImageField(blank=True, null=True, upload_to='icon-images/'),
        ),
        migrations.AlterField(
            model_name='chemicalsafetyprecaution',
            name='icon_image',
            field=models.ImageField(blank=True, null=True, upload_to='icon-images/'),
        ),
    ]
