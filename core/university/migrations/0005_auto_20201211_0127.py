# Generated by Django 3.1.4 on 2020-12-11 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_faq_financeaid'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='university',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='faq', to='university.university'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financeaid',
            name='university',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='aid', to='university.university'),
            preserve_default=False,
        ),
    ]
