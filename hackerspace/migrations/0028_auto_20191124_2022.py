# Generated by Django 2.2.6 on 2019-11-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0027_auto_20191124_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='str_location',
            field=models.CharField(default='2169 Mission St\n94110, San Francisco, CA, US', max_length=250, verbose_name='Location'),
        ),
    ]