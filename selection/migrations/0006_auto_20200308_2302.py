# Generated by Django 2.2.10 on 2020-03-08 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0005_auto_20200308_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='output',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='tool',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
