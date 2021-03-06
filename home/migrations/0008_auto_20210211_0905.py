# Generated by Django 3.1.6 on 2021-02-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210209_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='clients',
            new_name='spinner',
        ),
        migrations.RenameField(
            model_name='setting',
            old_name='spinners',
            new_name='spinner2',
        ),
        migrations.AddField(
            model_name='setting',
            name='spinner3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
