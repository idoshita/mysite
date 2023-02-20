from django import forms


class BookingForm(forms.Form):
    adlutnum = forms.IntegerField(label="大人人数",max_value=3,min_value=0,initial=1)
    childnum = forms.IntegerField(label="子供人数",max_value=3,min_value=0,initial=0)



class MaxNumForm(forms.Form):
    maxnum = forms.IntegerField(label="予約最大数")


class MaxNumeForm(forms.Form):
    maxnum = forms.IntegerField(label="予約最大数")


class DefaultValueForm(forms.Form):
    defaultvalue = forms.IntegerField(label="全日予約数")
