# Generated by Django 3.0.8 on 2020-07-24 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0002_consume'),
    ]

    operations = [
        migrations.AddField(
            model_name='consume',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
