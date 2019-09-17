# Generated by Django 2.2 on 2019-09-11 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='学生姓名')),
                ('student_major', models.CharField(blank=True, default='计算机', max_length=20, null=True, verbose_name='学生专业')),
                ('student_age', models.IntegerField(verbose_name='学生年龄')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Teacher')),
            ],
            options={
                'verbose_name': '学生表',
                'verbose_name_plural': '学生表',
            },
        ),
    ]
