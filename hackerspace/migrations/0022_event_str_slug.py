# Generated by Django 2.2.6 on 2019-11-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0021_auto_20191112_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='str_slug',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]