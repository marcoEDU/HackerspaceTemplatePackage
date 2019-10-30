# Generated by Django 2.2.6 on 2019-10-28 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date_repeating_end',
        ),
        migrations.RemoveField(
            model_name='event',
            name='one_original_event',
        ),
        migrations.RemoveField(
            model_name='event',
            name='str_repeating',
        ),
        migrations.AddField(
            model_name='event',
            name='int_series_endUNIX',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='int_series_startUNIX',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='str_series_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='text_series_timing',
            field=models.TextField(blank=True, null=True),
        ),
    ]