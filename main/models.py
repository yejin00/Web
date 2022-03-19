from django.db import models

# Create your models here.
class Cabbage(models.Model):
    년 = models.IntegerField(blank=True, null=True)
    월 = models.IntegerField(blank=True, null=True)
    배추상품 = models.IntegerField(blank=True, null=True)
    배추중품 = models.IntegerField(blank=True, null=True)
    서울 = models.IntegerField(blank=True, null=True)
    부산 = models.IntegerField(blank=True, null=True)
    대구 = models.IntegerField(blank=True, null=True)
    광주 = models.IntegerField(blank=True, null=True)
    대전 = models.IntegerField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    도매가격 = models.FloatField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    신선식품지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.IntegerField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균풍속 = models.FloatField(blank=True, null=True)
    합계일사량 = models.FloatField(blank=True, null=True)
    총지수전년동월비 = models.FloatField(blank=True, null=True)
    신선식품지수전년동월비 = models.FloatField(blank=True, null=True)
    배추상중 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cabbage'
        
class Onion(models.Model):
    년 = models.IntegerField(blank=True, null=True)
    월 = models.IntegerField(blank=True, null=True)
    양파상품 = models.IntegerField(blank=True, null=True)
    양파중품 = models.IntegerField(blank=True, null=True)
    서울 = models.IntegerField(blank=True, null=True)
    부산 = models.IntegerField(blank=True, null=True)
    대구 = models.IntegerField(blank=True, null=True)
    광주 = models.IntegerField(blank=True, null=True)
    대전 = models.IntegerField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    도매가격 = models.FloatField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    신선식품지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.IntegerField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균풍속 = models.FloatField(blank=True, null=True)
    합계일사량 = models.FloatField(blank=True, null=True)
    총지수전년동월비 = models.FloatField(blank=True, null=True)
    신선식품지수전년동월비 = models.FloatField(blank=True, null=True)
    양파상중 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onion'


class Pepper(models.Model):
    년 = models.IntegerField(blank=True, null=True)
    월 = models.IntegerField(blank=True, null=True)
    건고추상품 = models.IntegerField(blank=True, null=True)
    건고추중품 = models.IntegerField(blank=True, null=True)
    서울 = models.IntegerField(blank=True, null=True)
    부산 = models.IntegerField(blank=True, null=True)
    대구 = models.IntegerField(blank=True, null=True)
    광주 = models.IntegerField(blank=True, null=True)
    대전 = models.IntegerField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    도매가격 = models.FloatField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    신선식품지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.IntegerField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균풍속 = models.FloatField(blank=True, null=True)
    합계일사량 = models.FloatField(blank=True, null=True)
    총지수전년동월비 = models.FloatField(blank=True, null=True)
    신선식품지수전년동월비 = models.FloatField(blank=True, null=True)
    건고추상중 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pepper'


class Radish(models.Model):
    년 = models.IntegerField(blank=True, null=True)
    월 = models.IntegerField(blank=True, null=True)
    무상품 = models.IntegerField(blank=True, null=True)
    무중품 = models.IntegerField(blank=True, null=True)
    서울 = models.IntegerField(blank=True, null=True)
    부산 = models.IntegerField(blank=True, null=True)
    대구 = models.IntegerField(blank=True, null=True)
    광주 = models.IntegerField(blank=True, null=True)
    대전 = models.IntegerField(blank=True, null=True)
    면적 = models.IntegerField(blank=True, null=True)
    생산량 = models.IntegerField(blank=True, null=True)
    도매가격 = models.FloatField(blank=True, null=True)
    물가지수 = models.FloatField(blank=True, null=True)
    총지수전년누계비 = models.FloatField(blank=True, null=True)
    신선식품지수전년누계비 = models.FloatField(blank=True, null=True)
    평균기온 = models.FloatField(blank=True, null=True)
    평균최고기온 = models.FloatField(blank=True, null=True)
    평균최저기온 = models.FloatField(blank=True, null=True)
    평균상대습도 = models.BigIntegerField(blank=True, null=True)
    월합강수량 = models.FloatField(blank=True, null=True)
    평균풍속 = models.FloatField(blank=True, null=True)
    합계일사량 = models.FloatField(blank=True, null=True)
    총지수전년동월비 = models.FloatField(blank=True, null=True)
    신선식품지수전년동월비 = models.FloatField(blank=True, null=True)
    무상중 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'radish'
        

class CabbageMean(models.Model):
    년 = models.IntegerField(blank=True, null=True)
    월 = models.IntegerField(blank=True, null=True)
    상_도매가격 = models.FloatField(blank=True, null=True)
    중_도매가격 = models.FloatField(blank=True, null=True)
    상중_도매가격 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cabbage_mean'
        
class OnionMean(models.Model):
    년 = models.IntegerField(blank=True, null=True)
    월 = models.IntegerField(blank=True, null=True)
    상_도매가격 = models.FloatField(blank=True, null=True)
    중_도매가격 = models.FloatField(blank=True, null=True)
    상중_도매가격 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onion_mean'
        
class PepperMean(models.Model):
    년 = models.IntegerField(blank=True, null=True)
    월 = models.IntegerField(blank=True, null=True)
    상_도매가격 = models.FloatField(blank=True, null=True)
    중_도매가격 = models.FloatField(blank=True, null=True)
    상중_도매가격 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pepper_mean'
        
    
class RadishMean(models.Model):
    년 = models.IntegerField(blank=True, null=True)
    월 = models.IntegerField(blank=True, null=True)
    상_도매가격 = models.FloatField(blank=True, null=True)
    중_도매가격 = models.FloatField(blank=True, null=True)
    상중_도매가격 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'radish_mean'