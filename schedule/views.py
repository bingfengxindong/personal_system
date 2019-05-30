from django.shortcuts import render,HttpResponse
from django.views.generic.base import View
from .models import *

import datetime

class ScheduleIndexHandler(View):
    def get(self,request):
        scheduletypes = ScheduleType.all_scheduletype()
        context = {
            "title":"首页",
            "today":datetime.datetime.today().strftime("%Y-%m-%d"),
            "scheduletypes":scheduletypes,
        }
        return render(request=request,template_name="schedule_index.html",context=context)

class ScheduleListHandler(View):
    def get(self,request):
        scheduletypes = ScheduleType.all_scheduletype()
        scheduletimes = ScheduleTime.all_scheduletime().order_by("-pk")
        context = {
            "title":"列表",
            "scheduletypes":scheduletypes,
            "scheduletimes":scheduletimes,
        }
        return render(request=request,template_name="schedule_list.html",context=context)