from django.conf.urls import url,include
from django.views.decorators.csrf import csrf_exempt
from .views import *
from .async_views import *

urlpatterns = [
    url(r"^schedule_index",csrf_exempt(ScheduleIndexHandler.as_view()),name="schedule_index"),
    url(r"^schedule_list",csrf_exempt(ScheduleListHandler.as_view()),name="schedule_list"),

    # 异步
    url(r"^scheduletime_add",csrf_exempt(ScheduleTimeAddHandler.as_view()),name="scheduletime_add"),
    url(r"^scheduletype_get",csrf_exempt(ScheduleTimeGetHandler.as_view()),name="scheduletype_get"),
]