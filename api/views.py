import time

from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import JsonResponse
from api.models import Teacher,Student

# render 模板渲染
# Create your views here.

# 第一个视图
def test1(request):
    dict1 = {
        'name': 'zq',
        'age': 18,
        'major': 'computer'
    }
    return JsonResponse({'data':dict1})

def test2(request,year,month,day):
    return HttpResponse(str(year) + "/" + str(month) + "/" + str(day))

def test3(request): #302重定向
    # time.sleep(3000)
    return HttpResponseRedirect("http://127.0.0.1:8000/admin/")
    # return redirect("http://127.0.0.1:8000/admin/")

def test_index(request):
    return render(request,"index.html")

def test_teacher(request):
    # results = Teacher.objects.all()
    # results = Teacher.objects.values("teacher_name").distinct().order_by("teacher_name")
    # results = Teacher.objects.raw("select * from api_teacher")
    results = Teacher.objects.values("teacher_name")
    results2 = Teacher.objects.filter(teacher_age__exact=20).count()
    print(results)
    list_t = []
    for result in results:
        list_t.append(result)

    # for result in results:
    #     collections = {}
    #     collections['teacher_name'] = result.teacher_name
    #     collections['teacher_major'] = result.teacher_major
    #     collections['teacher_age'] = result.teacher_age
    #     list_t.append(collections)
    #     print(collections)
    # print(results)
    return JsonResponse({"data":list_t,'count':results2})

def test_teacher_add(request):
    # 方式一
    Teacher.objects.create(teacher_name="张清1",teacher_major="核动力",teacher_age=20)
    # 方式二
    t = Teacher(teacher_name="张清2",teacher_major="核动力",teacher_age=20)
    t.save()
    # 方式三
    dict_teacher = {
        'teacher_name' : "张清3",
        'teacher_major' : "核动力",
        'teacher_age' : 20
    }
    # ** 代表可变参数
    Teacher.objects.create(**dict_teacher)
    return JsonResponse({'status':200,'message':"Insert Success"})

def test_teacher_update(request):
    Teacher.objects.filter(id=3).update(teacher_major="大数据")
    return JsonResponse({'status':200,'message':"Update Success"})

def test_teacher_delete(request):
    Teacher.objects.filter(id=5).delete()
    return JsonResponse({'status':200,'message':"Delete Success"})

def test_query(request):

    # result = Teacher.objects.get(id=1)
    # print(result.teacher_name)
    # return JsonResponse({'status': 200, 'message': "Select Success"})

    # results = Teacher.objects.all().order_by("id") # 查询所有数据
    # results = Teacher.objects.all().filter(teacher_age__lte = 30) #年龄小于30的人
    results = Teacher.objects.all().filter(teacher_age__lte=30,teacher_name__contains='张')
    list_t = []
    for result in results:
        collections = {}
        collections['teacher_name'] = result.teacher_name
        collections['teacher_major'] = result.teacher_major
        collections['teacher_age'] = result.teacher_age
        list_t.append(collections)
    return JsonResponse({'status': 200, 'message': "Select Success",'data':list_t})

def find_teacher_age(request):
    stu = Student.objects.all()
    list_t = []
    for i in stu:
        # print(i.teacher)
        collections = {}
        collections['t_age'] = i.teacher.teacher_age
        list_t.append(collections)
    print(list_t)
    return JsonResponse({'data':"SUCCESS"})
