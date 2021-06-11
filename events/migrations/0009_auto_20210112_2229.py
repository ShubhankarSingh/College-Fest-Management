# Generated by Django 2.2 on 2021-01-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_is_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='meet_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
