# Generated by Django 4.0 on 2021-12-30 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_motherboard_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='vendor',
            field=models.CharField(max_length=255),
        ),
    ]
