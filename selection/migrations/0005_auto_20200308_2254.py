# Generated by Django 2.2.10 on 2020-03-08 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0004_auto_20190626_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='req',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]