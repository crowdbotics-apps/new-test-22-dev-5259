# Generated by Django 2.2.12 on 2020-05-31 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200530_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
