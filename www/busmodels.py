#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, order, cars.
'''

__author__ = 'Xu'

import time, uuid

from busorm import Model, StringField, BooleanField, FloatField, TextField, IntegerField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    telephone = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    usertype = IntegerField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    evaluation = StringField(ddl='varchar(50)')
    vip = BooleanField()
    created_at = FloatField(default=time.time)

class Order(Model):
    __table__ = 'orders'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    car_id = StringField(ddl='varchar(50)')
    order_from = StringField(ddl='varchar(50)')
    order_to = StringField(ddl='varchar(50)')
    order_acid = StringField(ddl='varchar(50)')
    price = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)

class Car(Model):
    __table__ = 'cars'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    seat = StringField(ddl='varchar(50)')
    car_acid = IntegerField()
    image = StringField(ddl='varchar(500)')
    content = TextField()
    evaluation = StringField(ddl='varchar(50)')
    location = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)
