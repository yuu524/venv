from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # ログアウトページ
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    
]