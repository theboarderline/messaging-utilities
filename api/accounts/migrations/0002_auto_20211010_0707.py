# Generated by Django 3.1.13 on 2021-10-10 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='city',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
