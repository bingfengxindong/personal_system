from django.contrib import admin
from django.conf.urls import url,include
from django.views.static import serve

import personal_system.settings as ps
import schedule

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^schedule/', include(("schedule.urls","schedule"),namespace="schedule")),
    url(r"^static/(?P<path>.*)",serve,{"document_root":ps.STATICFILES_DIRS[0]},name="static"),
    url(r"^media/(?P<path>.*)",serve,{"document_root":ps.MEDIA_ROOT},name="media"),
]
