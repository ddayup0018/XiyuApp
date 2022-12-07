# Generated by Django 4.1.3 on 2022-11-16 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jishi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('js_pic', models.CharField(default='logo.png', max_length=128, verbose_name='技师图片')),
                ('js_name', models.CharField(max_length=32, verbose_name='技师名称')),
                ('js_from', models.CharField(max_length=32, verbose_name='技师来自')),
                ('js_specialty', models.CharField(max_length=32, verbose_name='技师特长')),
                ('js_status', models.CharField(default='空闲', max_length=4, verbose_name='技师状态')),
            ],
            options={
                'verbose_name': '技师表',
                'db_table': 'jishi',
            },
        ),
        migrations.CreateModel(
            name='Taocan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tc_pic', models.CharField(default='logo.png', max_length=128, verbose_name='套餐图片')),
                ('tc_name', models.CharField(max_length=32, verbose_name='套餐名称')),
                ('tc_sale', models.IntegerField(default=0, verbose_name='已售')),
                ('tc_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='套餐价格')),
                ('tc_time', models.IntegerField(verbose_name='套餐时间')),
                ('tc_intraduce', models.CharField(max_length=128, verbose_name='套餐介绍')),
            ],
            options={
                'verbose_name': '套餐表',
                'db_table': 'taocan',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户表',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Dingdan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ding_status', models.CharField(max_length=6, verbose_name='订单状态')),
                ('startServer', models.BooleanField(default=False, verbose_name='是否开始服务')),
                ('jishi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dingdan_forjishi', to='quickstart.jishi')),
                ('taocan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dingdan_fortaocan', to='quickstart.taocan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dingdan_fortaocan', to='quickstart.users')),
            ],
            options={
                'verbose_name': '用户订单表',
                'db_table': 'dingdan',
            },
        ),
    ]
