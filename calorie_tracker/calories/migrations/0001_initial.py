# Generated by Django 3.0.8 on 2020-07-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('carbs', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('calories', models.IntegerField()),
            ],
        ),
    ]
