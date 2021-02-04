# Generated by Django 3.1.5 on 2021-01-08 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floattn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='type',
            field=models.CharField(choices=[('putin', 'Putin'), ('pullout', 'Pullout'), ('both', 'Both')], default='both', max_length=7),
        ),
    ]
