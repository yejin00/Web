from django.db import models

class Cab6(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cab6'


class Cab7(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cab7'


class Cab8(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cab8'


class Oni6(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oni6'


class Oni7(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oni7'


class Oni8(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oni8'
        
class Pep6(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pep6'


class Pep7(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pep7'


class Pep8(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pep8'


class Rad6(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rad6'


class Rad7(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rad7'


class Rad8(models.Model):
    지역 = models.TextField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rad8'
