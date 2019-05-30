from django.db import models
import uuid

# Create your models here.
class ScheduleTime(models.Model):
    st_id = models.UUIDField(verbose_name="编号")
    st_time = models.DateField(verbose_name="时间")
    st_type = models.ManyToManyField("ScheduleType",verbose_name="编号")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.st_time)

    class Meta:
        ordering = ["pk"]
        verbose_name = "计划时间表"
        verbose_name_plural = "计划时间表"

    @staticmethod
    def all_scheduletime():
        return ScheduleTime.objects.all()

    @staticmethod
    def add_scheduletime(**kwargs):
        scheduletimes = ScheduleTime.objects.filter(st_time=kwargs["time"])
        if not scheduletimes.exists():
            scheduletime = ScheduleTime.objects.create(st_id=uuid.uuid1(),st_time=kwargs["time"],)
        else:
            scheduletime = scheduletimes[0]
        if kwargs["stp_action"] == "add":
            scheduletime.st_type.add(kwargs["type"])
        elif kwargs["stp_action"] == "del":
            scheduletime.st_type.remove(kwargs["type"])

    @staticmethod
    def get_scheduletype_exist(**kwargs):
        scheduletimes = ScheduleTime.objects.filter(st_time=kwargs["time"])
        if scheduletimes.exists():
            if scheduletimes[0].st_type.filter(stp_id=kwargs["stp_pk"]).exists():
                ste = "y"
            else:
                ste = "n"
        else:
            ste = "n"
        return ste

class ScheduleType(models.Model):
    stp_id = models.UUIDField(verbose_name="编号")
    stp_type = models.CharField(max_length=200,verbose_name="类型")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.stp_type)

    class Meta:
        ordering = ["pk"]
        verbose_name = "计划类型表"
        verbose_name_plural = "计划类型表"

    @staticmethod
    def all_scheduletype():
        return ScheduleType.objects.all()

    @staticmethod
    def get_scheduletype(**kwargs):
        return ScheduleType.objects.get(stp_id=kwargs["stp_pk"])