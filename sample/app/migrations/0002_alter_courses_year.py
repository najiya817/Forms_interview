# Generated by Django 4.2.5 on 2023-09-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]
