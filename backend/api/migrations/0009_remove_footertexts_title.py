# Generated by Django 2.0.5 on 2018-06-22 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180622_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footertexts',
            name='title',
        ),
    ]
