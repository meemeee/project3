# Generated by Django 2.1.5 on 2019-11-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20191105_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, choices=[('s', 'small'), ('l', 'large')], default='', max_length=1),
        ),
    ]