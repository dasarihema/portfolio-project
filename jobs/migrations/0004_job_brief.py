# Generated by Django 2.1.5 on 2019-01-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job_project_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='brief',
            field=models.CharField(default='This is a brief project', max_length=200),
            preserve_default=False,
        ),
    ]
