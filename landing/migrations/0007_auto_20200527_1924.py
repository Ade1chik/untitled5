# Generated by Django 3.1a1 on 2020-05-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_houses_geo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='geo',
            field=models.CharField(default='Местоположение не указано', max_length=64, null=True),
        ),
    ]
