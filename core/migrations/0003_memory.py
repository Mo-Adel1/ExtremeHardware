# Generated by Django 4.0 on 2021-12-27 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20211226_1107'),
        ('core', '0002_case_cooler_cpu_gpu_motherboard_psu_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='store.product')),
                ('memory_type', models.CharField(max_length=255)),
                ('places', models.IntegerField()),
                ('size', models.IntegerField()),
                ('speed', models.IntegerField()),
            ],
            bases=('store.product',),
        ),
    ]
