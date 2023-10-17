# Generated by Django 3.2.20 on 2023-10-13 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0034_alter_xblockskills_usage_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='industryjobskill',
            name='is_blacklisted',
            field=models.BooleanField(default=False, help_text='Should this job skill be ignored?'),
        ),
        migrations.AddField(
            model_name='jobskills',
            name='is_blacklisted',
            field=models.BooleanField(default=False, help_text='Should this job skill be ignored?'),
        ),
    ]
