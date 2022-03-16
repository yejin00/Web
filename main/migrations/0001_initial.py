# Generated by Django 4.0.3 on 2022-03-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabbage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('년', models.IntegerField(blank=True, null=True)),
                ('월', models.IntegerField(blank=True, null=True)),
                ('배추상품', models.IntegerField(blank=True, null=True)),
                ('배추중품', models.IntegerField(blank=True, null=True)),
                ('서울', models.IntegerField(blank=True, null=True)),
                ('부산', models.IntegerField(blank=True, null=True)),
                ('대구', models.IntegerField(blank=True, null=True)),
                ('광주', models.IntegerField(blank=True, null=True)),
                ('대전', models.IntegerField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('도매가격', models.FloatField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('신선식품지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.IntegerField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균풍속', models.FloatField(blank=True, null=True)),
                ('합계일사량', models.FloatField(blank=True, null=True)),
                ('총지수전년동월비', models.FloatField(blank=True, null=True)),
                ('신선식품지수전년동월비', models.FloatField(blank=True, null=True)),
                ('배추상중', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cabbage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Onion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('년', models.IntegerField(blank=True, null=True)),
                ('월', models.IntegerField(blank=True, null=True)),
                ('양파상품', models.IntegerField(blank=True, null=True)),
                ('양파중품', models.IntegerField(blank=True, null=True)),
                ('서울', models.IntegerField(blank=True, null=True)),
                ('부산', models.IntegerField(blank=True, null=True)),
                ('대구', models.IntegerField(blank=True, null=True)),
                ('광주', models.IntegerField(blank=True, null=True)),
                ('대전', models.IntegerField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('도매가격', models.FloatField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('신선식품지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.IntegerField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균풍속', models.FloatField(blank=True, null=True)),
                ('합계일사량', models.FloatField(blank=True, null=True)),
                ('총지수전년동월비', models.FloatField(blank=True, null=True)),
                ('신선식품지수전년동월비', models.FloatField(blank=True, null=True)),
                ('양파상중', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'onion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pepper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('년', models.IntegerField(blank=True, null=True)),
                ('월', models.IntegerField(blank=True, null=True)),
                ('건고추상품', models.IntegerField(blank=True, null=True)),
                ('건고추중품', models.IntegerField(blank=True, null=True)),
                ('서울', models.IntegerField(blank=True, null=True)),
                ('부산', models.IntegerField(blank=True, null=True)),
                ('대구', models.IntegerField(blank=True, null=True)),
                ('광주', models.IntegerField(blank=True, null=True)),
                ('대전', models.IntegerField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('도매가격', models.FloatField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('신선식품지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.IntegerField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균풍속', models.FloatField(blank=True, null=True)),
                ('합계일사량', models.FloatField(blank=True, null=True)),
                ('총지수전년동월비', models.FloatField(blank=True, null=True)),
                ('신선식품지수전년동월비', models.FloatField(blank=True, null=True)),
                ('건고추상중', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pepper',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Radish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('년', models.IntegerField(blank=True, null=True)),
                ('월', models.IntegerField(blank=True, null=True)),
                ('무상품', models.IntegerField(blank=True, null=True)),
                ('무중품', models.IntegerField(blank=True, null=True)),
                ('서울', models.IntegerField(blank=True, null=True)),
                ('부산', models.IntegerField(blank=True, null=True)),
                ('대구', models.IntegerField(blank=True, null=True)),
                ('광주', models.IntegerField(blank=True, null=True)),
                ('대전', models.IntegerField(blank=True, null=True)),
                ('면적', models.IntegerField(blank=True, null=True)),
                ('생산량', models.IntegerField(blank=True, null=True)),
                ('도매가격', models.FloatField(blank=True, null=True)),
                ('물가지수', models.FloatField(blank=True, null=True)),
                ('총지수전년누계비', models.FloatField(blank=True, null=True)),
                ('신선식품지수전년누계비', models.FloatField(blank=True, null=True)),
                ('평균기온', models.FloatField(blank=True, null=True)),
                ('평균최고기온', models.FloatField(blank=True, null=True)),
                ('평균최저기온', models.FloatField(blank=True, null=True)),
                ('평균상대습도', models.BigIntegerField(blank=True, null=True)),
                ('월합강수량', models.FloatField(blank=True, null=True)),
                ('평균풍속', models.FloatField(blank=True, null=True)),
                ('합계일사량', models.FloatField(blank=True, null=True)),
                ('총지수전년동월비', models.FloatField(blank=True, null=True)),
                ('신선식품지수전년동월비', models.FloatField(blank=True, null=True)),
                ('무상중', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'radish',
                'managed': False,
            },
        ),
    ]