# Generated by Django 4.0.3 on 2022-04-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CabbageApp', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            ],
            options={
                'db_table': 'popup',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
