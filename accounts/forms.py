from django import forms
from allauth.account.forms import SignupForm
from django.core.validators import RegexValidator
from accounts.models import SexChoices

#djangoのSignupFormは、adminで作るユーザー登録がadminによらずできるようになるライブラリ

#forms.pyは、html内の記述がPOSTで送られた際に、データベースに保存する為の設定を記述する場所。
#djangoのformsというライブラリのおかげです。



class ProfileForm(forms.Form):

    name = forms.CharField(label="名前", max_length=150)
    address = forms.CharField(label="住所", max_length=150)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    tel = forms.CharField(label="電話番号",validators = [phoneNumberRegex], max_length = 16)



class SignupUserForm(SignupForm):#allauthのサインアップ機能を継承する。
    name = forms.CharField(label="名前", max_length=150)
    address = forms.CharField(label="住所", max_length=150)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    tel = forms.CharField(label="電話番号",validators = [phoneNumberRegex], max_length = 16)

    gender = forms.fields.ChoiceField(
        choices=SexChoices.choices,
        required=True,
        label='性別',
        # widget=forms.widgets.Select,
    )
    #サインアップ時に所属など追加したい項目があれば、ここに追加する。

    def save(self,request):#サインアップボタンがクリックされた時の動作を下記で記載している。
        user = super(SignupUserForm,self).save(request)
        user.name = self.cleaned_data["name"]#上記のSignupUserFormで設定した内容を登録する記述である。
        user.address = self.cleaned_data["address"]
        user.tel = self.cleaned_data["tel"]
        user.gender = self.cleaned_data["gender"]
        user.save()#上記の設定した内容を保存する記述である。
        return user
