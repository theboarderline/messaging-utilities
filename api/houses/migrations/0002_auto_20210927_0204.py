# Generated by Django 3.1.13 on 2021-09-27 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
        ('leads', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='deal_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.dealtype'),
        ),
        migrations.AddField(
            model_name='house',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.member'),
        ),
    ]
