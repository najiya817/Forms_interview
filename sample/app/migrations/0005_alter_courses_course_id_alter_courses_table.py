# Generated by Django 4.2.5 on 2023-10-04 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_courses_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='app.register'),
        ),
        migrations.AlterModelTable(
            name='courses',
            table='courses',
        ),
    ]
