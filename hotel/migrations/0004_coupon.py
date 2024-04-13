# Generated by Django 5.0.3 on 2024-04-12 07:06

import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_remove_hotel_tags_hotel_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('type', models.CharField(default='Percentage', max_length=100)),
                ('discount', models.IntegerField(default=1)),
                ('redemptions', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=10, max_length=20, prefix='', unique=True)),
            ],
        ),
    ]