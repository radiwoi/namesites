# Generated by Django 2.0.5 on 2018-06-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180611_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterTexts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('read_more_words', models.IntegerField()),
            ],
        ),
    ]
