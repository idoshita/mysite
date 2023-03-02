from django.shortcuts import render, redirect
from django.views import View
from accounts.models import CustomUser
from accounts.forms import ProfileForm,SignupUserForm
from allauth.account import views
from django.contrib.auth.mixins import LoginRequiredMixin

# LoginRequiredMixinのライブラリを使うことで、ログアウト状態で、メインコンテンツに遷移した場合には、ログイン画面に遷移するようになる。


class ProfileView(LoginRequiredMixin, View):
    def get(self, request,*args,**kwargs):#GETに必要な記述
        user_data = CustomUser.objects.get(id=request.user.id) # データベースからカスタムユーザーを取得する。
        return render(request,"accounts/profile.html",{# この分により、GETで呼ばれた際に、profile.htmlを表示する。
        "user_data":user_data,
        })



class EditView(LoginRequiredMixin, View):
    def get(self, request,*args,**kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)# データベースからカスタムユーザーを取得する。
        print(user_data)
        form = ProfileForm(
            request.POST or None,# GETで呼び出した際には、Noneなので、単純なデータベースを表示する。POSTされた際にformを表示。
            initial={# initialは、インスタンスのフォーム初期化時に設定するものである。
                "name":user_data.name,
                "address":user_data.address,
                "tel":user_data.tel,
            }
        )

        return render(request,"accounts/profile_edit.html",{
            "form":form,
        })


    def post(self, request,*args,**kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():# .is_validでformの内容をチェックする
            user_data = CustomUser.objects.get(id=request.user.id)
            user_data.name = form.cleaned_data["name"]#フォームされた時の処理なので、.cleaned_dataで、formで送られた情報を取得する。
            user_data.address = form.cleaned_data["address"]
            user_data.tel = form.cleaned_data["tel"]
            user_change = CustomUser(id=user_data.id,password=user_data.password,email=user_data.email,name=user_data.name,address=user_data.address,tel=user_data.tel,gender=user_data.gender,is_staff=user_data.is_staff,is_active=user_data.is_active)
            # if request.FILES.get("image"):#もし画像が変更された場合は、
            #     user_data.image = request.FILES.get("image")
            user_change.save()#.cleaned_dataで変更になったデータをセーブ(保存)する。
            return redirect("profile")#セーブが完了したら、プロフィールに遷移します。


        return render(request,"accounts/profile.html",{
            "form":form,
        })


class LoginView(views.LoginView):#allauthのログインビューを継承する。これで簡単にログインが可能となる。
    template_name = "accounts/login.html"


class LogoutView(views.LogoutView):#allauthのログアウトビューを継承する。これで簡単にログインが可能となる。
    template_name = "accounts/logout.html"

    def post(self,*args,**kwargs):
        if self.request.user.is_authenticated:#userのログイン状態を把握して、「もしログイン状態でポストされたなら」
            self.logout()#ログアウトする。
            return redirect("/")#ログアウトしたらトップページに遷移する。


class SignupView(views.SignupView):#allauthのサインアップビューを継承する。これで簡単にサインアップが可能となる。
    template_name = "accounts/signup.html"
    form_class = SignupUserForm #この記述により、オリジナルのフォームを利用する事ができるようになる。

