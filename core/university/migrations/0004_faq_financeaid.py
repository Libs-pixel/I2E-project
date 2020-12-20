# Generated by Django 3.1.4 on 2020-12-11 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_degree_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Frequently asked Question', max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FinanceAid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
