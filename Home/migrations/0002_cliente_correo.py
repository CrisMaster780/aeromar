# Generated by Django 4.2.1 on 2023-06-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
