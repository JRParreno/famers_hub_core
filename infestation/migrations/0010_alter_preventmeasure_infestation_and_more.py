# Generated by Django 4.1 on 2022-09-19 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infestation', '0009_alter_preventmeasure_prevent_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preventmeasure',
            name='infestation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infestaion_prevent_measure', to='infestation.infestation'),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='infestation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infestaion_symptom', to='infestation.infestation'),
        ),
    ]
