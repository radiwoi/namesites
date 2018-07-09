# Generated by Django 2.0.5 on 2018-07-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180622_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlicknamnFooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, null=True)),
                ('position', models.CharField(max_length=64)),
                ('names', models.TextField(null=True)),
                ('read_more_words', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Flicknamn Footer Text',
            },
        ),
        migrations.CreateModel(
            name='PojknamnFooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, null=True)),
                ('position', models.CharField(max_length=64)),
                ('names', models.TextField(null=True)),
                ('read_more_words', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Pojknamn Footer Text',
            },
        ),
    ]
