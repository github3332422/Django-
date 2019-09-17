from django.contrib import admin
from shop.models import ShopGoods
# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','goods_name','goods_count','goods_price','goods_type','goods_birth')
    # list_editable = ('goods_count',)
    # list_editable = ('goods_price',)
    # list_editable = ('goods_birth',)
    fields = ('goods_name','goods_count','goods_price','goods_type','goods_birth')

admin.site.register(ShopGoods,ShopAdmin)
