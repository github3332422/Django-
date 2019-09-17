from django.test import TestCase
import requests
# Create your tests here.
data = {
    "goods_name": "康师傅",
    "goods_count": 10,
    "goods_price": 5,
    "goods_type": "饮品",
    "goods_birth": "中国台湾"
}
data2 = {
    'goods_name': '康师傅',
    'goods_type': '饮品',
    'goods_birth': '中国台湾'
}
url = "http://127.0.0.1:8000/shop/shop_goods/"
while(True):
    method = input("请输入请求方法")
    if method == 'get':
        req = requests.get(url=url, params=data2)
        print(req.status_code)
        print(req.text)
    elif method == 'post':
        req = requests.post(url=url, data=data)
        print(req.status_code)
        print(req.text)
