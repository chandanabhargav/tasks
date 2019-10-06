# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tasks.models import User, Task

# Register your models here.
admin.site.register(User)
admin.site.register(Task)