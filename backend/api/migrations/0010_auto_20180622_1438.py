# Generated by Django 2.0.5 on 2018-06-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_footertexts_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='footertexts',
            name='boy_title',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='footertexts',
            name='girl_title',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
