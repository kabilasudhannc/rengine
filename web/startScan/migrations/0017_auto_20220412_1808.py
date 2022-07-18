# Generated by Django 3.2.4 on 2022-04-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0016_directoryscan_scanned_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='endpoint_subscan_ids',
            field=models.ManyToManyField(blank=True, related_name='endpoint_subscan_ids', to='startScan.SubScan'),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='vuln_subscan_ids',
            field=models.ManyToManyField(blank=True, related_name='vuln_subscan_ids', to='startScan.SubScan'),
        ),
    ]