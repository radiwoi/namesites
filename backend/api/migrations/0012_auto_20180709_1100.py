# Generated by Django 2.0.5 on 2018-07-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_flicknamnfootertext_pojknamnfootertext'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flicknamnfootertext',
            options={'verbose_name_plural': 'Flicknamn Footer Texts'},
        ),
        migrations.AlterModelOptions(
            name='pojknamnfootertext',
            options={'verbose_name_plural': 'Pojknamn Footer Texts'},
        ),
        migrations.AlterField(
            model_name='email',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]