"""dj02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from api import views as api_v
urlpatterns = [
    path('test/',api_v.test1),
    # path('test2/',api_v.test2),
    # path('<int:year>/<int:month>/<int:day>',api_v.test2), #动态路由
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-1]{1}[0-9]{1})/(?P<day>[0-3]{1}[0-9]{1})',api_v.test2)
    re_path('(?P<year>[0-9]{4})/(?P<month>0[0-9]|1[0-2])/(?P<day>[0-3]{1}[0-9]{1})',api_v.test2),
    path('test3/',api_v.test3),
    path('test4/',api_v.test_index),
    path('test_teacher/',api_v.test_teacher),
    path('teacherAdd/',api_v.test_teacher_add),
    path('teacherUpdate/',api_v.test_teacher_update),
    path('teacherDelete/',api_v.test_teacher_delete),
    path('teacherSelect/',api_v.test_query),
    path('query_tagin/',api_v.find_teacher_age),
]


