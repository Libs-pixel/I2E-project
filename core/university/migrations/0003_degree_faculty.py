# Generated by Django 3.1.4 on 2020-12-11 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_university_headnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualifications', models.CharField(max_length=50)),
                ('information', models.TextField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='degrees', to='university.university')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('fee', models.IntegerField()),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculties', to='university.degree')),
            ],
        ),
    ]
