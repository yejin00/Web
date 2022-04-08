# Generated by Django 3.2 on 2022-04-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CabbageApp', '0005_cabbagebusan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cab6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수_전년누계비', models.FloatField(blank=True, db_column='총지수 전년누계비', null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cab6',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cab7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수_전년누계비', models.FloatField(blank=True, db_column='총지수 전년누계비', null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cab7',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cab8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수_전년누계비', models.FloatField(blank=True, db_column='총지수 전년누계비', null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cab8',
                'managed': False,
            },
        ),
    ]
