# Generated by Django 3.1.6 on 2021-02-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210209_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='clients',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='setting',
            name='gotop',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='setting',
            name='spinners',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]