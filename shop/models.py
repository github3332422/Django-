from django.db import models

# Create your models here.
class ShopGoods(models.Model):
    id = models.AutoField(primary_key=True)
    goods_name  = models.CharField(max_length=20,verbose_name="商品名字",null=True,blank=True)
    goods_count = models.IntegerField(verbose_name="商品数量",default=0)
    goods_price = models.FloatField(verbose_name="商品价格",default=0)
    goods_type  = models.CharField(max_length=20,verbose_name="商品类型",null=True,blank=True)
    goods_birth = models.CharField(max_length=20,verbose_name="商品产地",null=True,blank=True)
    def __str__(self):
        return self.goods_name
    class Meta:
        verbose_name = "商品表"
        verbose_name_plural = verbose_name
