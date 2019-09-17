from django.shortcuts import render
from django.views import View   #引入通用视图
from django.http import JsonResponse,QueryDict  # QueryDict
from shop.models import ShopGoods as SG
from django.views.decorators.csrf import csrf_exempt #引入跨栈请求
import json
# Create your views here.

def goods_list(request):
    return render(request,'good_list.html')

class ShopGoods(View):
    @csrf_exempt #装饰器
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def get(self,request):
        # http://127.0.0.1:8000/shop/shop_goods/?goods_type=饮品&goods_name=康师傅
        goods_name = request.GET.get("goods_name",'')
        goods_type = request.GET.get("goods_type",'')
        goods_birth = request.GET.get("goods_birth", '')
        results = SG.objects.filter(goods_type__contains=goods_type,goods_name__contains=goods_name,goods_birth__contains=goods_birth)
        # results = SG.objects.all() #全部查询
        list_result = []
        for i in results:
            collections = {}
            collections['goods_name'] = i.goods_name
            collections['goods_count'] = i.goods_count
            collections['goods_price'] = i.goods_price
            collections['goods_type'] = i.goods_type
            collections['goods_birth'] = i.goods_birth
            list_result.append(collections)
        return JsonResponse({'message':'success get','data':list_result,'code':200})

    def post(self,request):
        # SG.objects.create(goods_name="康师傅",goods_count=10,goods_price=1.5,goods_type="饮品",goods_birth="中国台湾")
        '''
        获取前端发送过来的请求
        '''
        goods_name = request.POST.get("goods_name")
        goods_count = request.POST.get("goods_count")
        goods_price = request.POST.get("goods_price")
        goods_type = request.POST.get("goods_type")
        goods_birth = request.POST.get("goods_birth")
        check_add = SG.objects.filter(goods_name=goods_name,goods_price=goods_price,goods_type=goods_type,goods_birth=goods_birth)
        if check_add:
            history_count = check_add[0].goods_count
            new_count = int(goods_count) + history_count
            check_add.update(goods_count=new_count)
            return JsonResponse({'message':'该商品已经存在','data':'更新后的总数%d'%new_count})
        else:
            sg_create = SG(goods_name=goods_name,goods_count=goods_count,goods_price=goods_price,goods_type=goods_type,goods_birth=goods_birth)
            sg_create.save()
            return JsonResponse({'data':'success post'})

    def put(self,request):
        put_result = QueryDict(request.body)
        goods_name = put_result.get("goods_name")
        goods_count = put_result.get("goods_count")
        goods_price = put_result.get("goods_price")
        goods_type = put_result.get("goods_type")
        goods_birth = put_result.get("goods_birth")
        # data = eval(put_result)["data"]
        # name_list = ["goods_name","goods_count","goods_price","goods_type","goods_birth"]
        # dict_result = zip(name_list,data)
        SG.objects.filter(goods_name=goods_name).update(goods_name=goods_name,goods_count=goods_count,goods_price=goods_price,goods_type=goods_type,goods_birth=goods_birth)# * 代表元组 ** 代表字典
        return JsonResponse({'data':'success put'})

    def delete(self,request):
        del_result= QueryDict(request.body) #获取前端请求的data的所有数据
        goods_name = del_result.get("goods_name")
        isSingle = del_result.get("isSingle","")
        print(isSingle,type(isSingle))
        if isSingle == '':
            SG.objects.filter(goods_name=goods_name).delete()
            return JsonResponse({'data': 'success delete One'})
        elif isSingle == '1':
            SG.objects.filter(goods_name=json.loads(goods_name)[0]).delete()
            return JsonResponse({'data': 'success delete OOne'})
        else:
            names = eval(goods_name)
            for name in names:
                SG.objects.filter(goods_name=name).delete()
            return JsonResponse({'data':'success delete All'})


