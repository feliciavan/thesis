# Generated by Django 2.2.2 on 2019-06-26 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0003_auto_20190625_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
