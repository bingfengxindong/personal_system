from django.shortcuts import render,HttpResponse
from django.views.generic.base import View
from .models import *

class ScheduleTimeAddHandler(View):
    def post(self,request):
        st_time = request.POST.get("st_time")
        stp_pk = request.POST.get("stp_pk")
        stp_action = request.POST.get("stp_action")
        scheduletype = ScheduleType.objects.get(stp_id=stp_pk)
        ScheduleTime.add_scheduletime(time=st_time,type=scheduletype,stp_action=stp_action)
        return HttpResponse("OK")

class ScheduleTimeGetHandler(View):
    def post(self,request):
        st_time = request.POST.get("st_time")
        stp_pk = request.POST.get("stp_pk")
        ste = ScheduleTime.get_scheduletype_exist(time=st_time,stp_pk=stp_pk)
        return HttpResponse(ste)