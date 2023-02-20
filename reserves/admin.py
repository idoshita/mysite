from django.contrib import admin
from .models import Booking,DefaultValue,MaxNum


admin.site.register(Booking)#adminでmodels.pyに追加したBookingクラスを編集できるようにする設定
admin.site.register(DefaultValue)#adminでmodels.pyに追加したBookingクラスを編集できるようにする設定
admin.site.register(MaxNum)#adminでmodels.pyに追加したBookingクラスを編集できるようにする設定