# Generated by Django 2.1.5 on 2019-11-06 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_auto_20191106_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, choices=[('s', 'small'), ('l', 'large')], default='s', max_length=1),
        ),
    ]