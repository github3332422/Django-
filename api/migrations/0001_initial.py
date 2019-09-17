# Generated by Django 2.2 on 2019-09-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='教师姓名')),
                ('teacher_major', models.CharField(blank=True, default='计算机', max_length=20, null=True, verbose_name='主修专业')),
                ('teacher_age', models.IntegerField(verbose_name='教师年龄')),
            ],
            options={
                'verbose_name': '老师表',
                'verbose_name_plural': '老师表',
            },
        ),
    ]
