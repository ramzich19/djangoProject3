# Generated by Django 3.1.5 on 2021-01-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210118_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=None, null=True, upload_to='images/', verbose_name='Photo'),
        ),
    ]
