# Generated by Django 2.2 on 2021-03-06 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_dojo_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='old dojo'),
        ),
    ]
