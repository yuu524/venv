from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('mainmenu/', views.mainmenu_views, name='mainmenu'),  # メインメニュー用ビュー
    path('upload/', views.upload, name='upload'), 
    path("upload_image/", views.upload_image, name="upload_image"),  # アップロード処理
    path("result/", views.result, name="result"),  # 結果ページ
    path('settings/', views.settings_view, name='settings'),
    path('history/', views.history_views, name='history'),
    path('languageSelection/', views.language_selection, name='language_selection'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)