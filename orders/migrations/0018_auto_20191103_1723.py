# Generated by Django 2.2.6 on 2019-11-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20191103_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdinnerplatters',
            name='ref',
            field=models.CharField(default='na', max_length=16),
        ),
        migrations.AddField(
            model_name='orderpasta',
            name='ref',
            field=models.CharField(default='na', max_length=16),
        ),
        migrations.AddField(
            model_name='ordersalads',
            name='ref',
            field=models.CharField(default='na', max_length=16),
        ),
        migrations.AddField(
            model_name='ordersubs',
            name='ref',
            field=models.CharField(default='na', max_length=16),
        ),
    ]