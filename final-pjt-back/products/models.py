from django.db import models

# Create your models here.


# 정기 예금 상품
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    mtrt_int = models.TextField()
    views_count = models.IntegerField(default=0, null=True)
    

# 정기 예금 상품 옵션
class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete = models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=100)
    save_trm = models.IntegerField(null=True)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)

# 정기 적금상품
class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    mtrt_int = models.TextField()
    views_count = models.IntegerField(default=0, null=True)

# 정기 적금 상품 옵션
class SavingOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(SavingProducts, on_delete = models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=100)
    save_trm = models.IntegerField(null=True)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)