# Generated by Django 4.0.3 on 2022-03-17 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cabbage',
            table='배추',
        ),
        migrations.AlterModelTable(
            name='onion',
            table='양파',
        ),
        migrations.AlterModelTable(
            name='pepper',
            table='건고추',
        ),
        migrations.AlterModelTable(
            name='radish',
            table='무',
        ),
    ]