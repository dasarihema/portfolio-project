# Generated by Django 2.1.5 on 2019-02-06 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20190206_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='brief',
            field=models.CharField(max_length=400),
        ),
    ]
