# Generated by Django 3.1.4 on 2020-12-11 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0007_faculty_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='duration',
            field=models.IntegerField(default=4),
        ),
    ]
