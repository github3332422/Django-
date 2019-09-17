from django.db import models

# Create your models here.
# 关系映射模型 用来用代码生成数据库

class Teacher(models.Model):
    id = models.AutoField(primary_key=True) # 主键自增长
    teacher_name = models.CharField(max_length=20,verbose_name="教师姓名",null=True,blank=True)
    teacher_major = models.CharField(max_length= 20,verbose_name="主修专业",default="计算机",null=True,blank=True)
    teacher_age = models.IntegerField(verbose_name="教师年龄")

    class Meta:
        verbose_name = "老师表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    id = models.AutoField(primary_key=True)  # 主键自增长
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=20, verbose_name="学生姓名", null=True, blank=True)
    student_major = models.CharField(max_length=20, verbose_name="学生专业", default="计算机", null=True, blank=True)
    student_age = models.IntegerField(verbose_name="学生年龄")

    class Meta:
        verbose_name = "学生表"
        verbose_name_plural = verbose_name
