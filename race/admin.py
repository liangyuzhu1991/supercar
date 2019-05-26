# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Race)
# Register your models here.
