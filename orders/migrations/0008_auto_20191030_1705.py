# Generated by Django 2.2.6 on 2019-10-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20191030_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toppings',
            name='steak_subs_extra',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='toppings',
            name='subs_extra',
            field=models.BooleanField(null=True),
        ),
    ]
