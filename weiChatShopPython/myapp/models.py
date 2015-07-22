# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AccountLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.CharField(max_length=50, blank=True)
    pay = models.IntegerField(blank=True, null=True)
    cart_id = models.IntegerField(unique=True, blank=True, null=True)
    paytime = models.DateTimeField(blank=True, null=True)
    payip = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'account_log'


class BookCart(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.CharField(max_length=50, blank=True)
    addr_id = models.IntegerField(blank=True, null=True)
    book_id = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    payment = models.FloatField(blank=True, null=True)
    send_status = models.IntegerField(blank=True, null=True)
    should_pay = models.FloatField(blank=True, null=True)
    addip = models.CharField(max_length=50, blank=True)
    addtime = models.DateTimeField(blank=True, null=True)
    payip = models.CharField(max_length=50, blank=True)
    paytime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_cart'


class BookClass(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=100, blank=True)
    describe = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'book_class'


class BookInfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    describe = models.CharField(max_length=500)
    list = models.TextField(blank=True)
    prelist = models.CharField(max_length=500, blank=True)
    path = models.CharField(max_length=300, blank=True)
    stock = models.IntegerField(blank=True, null=True)
    sell = models.IntegerField(blank=True, null=True)
    hot = models.IntegerField(blank=True, null=True)
    classify_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    freight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_info'


class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    uid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    detail_addr = models.CharField(max_length=50)
    postalcode = models.IntegerField()
    require = models.CharField(max_length=300, blank=True)
    addip = models.CharField(max_length=50, blank=True)
    addtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'
