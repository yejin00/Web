# Generated by Django 4.0.3 on 2022-04-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SettingsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oni6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'oni6',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oni7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'oni7',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Oni8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'oni8',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pep6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pep6',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pep7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pep7',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pep8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pep8',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rad6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rad6',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rad7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rad7',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rad8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('지역', models.TextField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rad8',
                'managed': False,
            },
        ),
    ]