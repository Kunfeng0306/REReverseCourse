# Generated by Django 2.0 on 2018-01-28 12:32

import accounts.helper
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='班级名称')),
            ],
            options={
                'verbose_name': '班级信息',
                'verbose_name_plural': '班级信息',
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='学生姓名')),
                ('stu_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='学号')),
                ('banned', models.BooleanField(default=False, verbose_name='是否停用')),
                ('school_classes', models.ManyToManyField(to='accounts.SchoolClass')),
                ('user', models.OneToOneField(on_delete=models.SET(accounts.helper.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='教师姓名')),
                ('tch_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='教工号')),
                ('banned', models.BooleanField(default=False, verbose_name='是否停用')),
                ('user', models.OneToOneField(on_delete=models.SET(accounts.helper.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '教师信息',
                'verbose_name_plural': '教师信息',
                'ordering': ('create_date',),
            },
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='head_teacher',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Teacher', verbose_name='班主任'),
        ),
    ]
