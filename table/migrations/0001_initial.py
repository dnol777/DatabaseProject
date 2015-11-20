# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contains',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.ForeignKey(to='table.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('active', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('stockQuantity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Supplys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.ForeignKey(to='table.Product')),
                ('supplier_id', models.ForeignKey(to='table.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('address', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('email', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(to='table.User'),
        ),
        migrations.AddField(
            model_name='contains',
            name='order_id',
            field=models.ForeignKey(to='table.Orders'),
        ),
        migrations.AddField(
            model_name='contains',
            name='product_id',
            field=models.ForeignKey(to='table.Product'),
        ),
    ]
