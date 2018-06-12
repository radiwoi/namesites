# Generated by Django 2.0.5 on 2018-06-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180608_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popularname',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='popularname',
            name='name',
        ),
        migrations.AddField(
            model_name='boyname',
            name='popular',
            field=models.ManyToManyField(related_name='boy_names', to='api.PopularName'),
        ),
        migrations.AddField(
            model_name='girlname',
            name='popular',
            field=models.ManyToManyField(related_name='girl_names', to='api.PopularName'),
        ),
    ]