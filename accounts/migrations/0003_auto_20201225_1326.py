# Generated by Django 2.2 on 2020-12-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201203_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default_profile.jpg', null=True, upload_to='images'),
        ),
    ]
