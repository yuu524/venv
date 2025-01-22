from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
#from .forms import UserRegistrationForm
#from .models import Language
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('mainmenu')  # ログイン後にリダイレクトするページ
        else:
            # フォームが無効な場合、カスタムエラーメッセージを設定
            error_message = "ユーザー名またはパスワードが間違っています。"
            return render(request, 'user/login.html', {'form': form, 'error': error_message})
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})



def logout_view(request):
    logout(request)  # ログアウト処理
    return redirect('login')  # ログインページにリダイレクト

def register(request):
    return render(request, 'user/register.html')  # 新規登録用テンプレートを返す


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '登録が完了しました。ログインしてください。')
            return redirect('login')  # ログインページのURL名に置き換えてください
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})



from django.contrib.auth.views import LoginView
from django.utils import translation

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user_language = self.request.user.language
        translation.activate(user_language)
        self.request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        return response


