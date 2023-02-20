from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from accounts.models import CustomUser
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.CASCADE, blank=True, null=True)
    childnum = models.PositiveIntegerField("子供予約数",default=0,blank=True,validators=[MaxValueValidator(3)])
    adlutnum = models.PositiveIntegerField("大人予約数",default=1,blank=True,validators=[MaxValueValidator(3)])
    start = models.DateTimeField("開始時間",default=timezone.now)
    end = models.DateTimeField("終了時間",default=timezone.now)
    active = models.BooleanField("取消情報",default=True)

    def __str__(self):
        start = timezone.localtime(self.start).strftime("%Y/%m/%d %H:%M") #localtimeを利用することでDjangoで設定したタイムゾーンの時間に変更される。
        end = timezone.localtime(self.end).strftime("%Y/%m/%d %H:%M")

        return f"{self.user}{start}～{end}"#adminの管理画面で、予約した名前と予約した時間が表示される。


class MaxNum(models.Model):
    maxnum = models.PositiveIntegerField("予約最大数",blank=True)
    starts = models.DateTimeField("開始時間",default=timezone.now)
    ends = models.DateTimeField("終了時間",default=timezone.now)

    def __str__(self):
        starts = timezone.localtime(self.starts).strftime("%Y/%m/%d %H:%M") #localtimeを利用することでDjangoで設定したタイムゾーンの時間に変更される。
        ends = timezone.localtime(self.ends).strftime("%Y/%m/%d %H:%M")

        return f"{starts}～{ends}{self.maxnum}"#adminの管理画面で、予約した名前と予約した時間が表示される。


class DefaultValue(models.Model):
    defaultvalue = models.IntegerField("全日予約数",blank=True)

    def __str__(self):
        return f"{self.defaultvalue}"
