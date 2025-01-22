from django.utils import translation

class SetLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:  # ユーザーがログインしている場合
            user_language = request.user.language  # ユーザーの言語設定を取得
            translation.activate(user_language)  # 言語を有効化
            request.LANGUAGE_CODE = user_language
        return self.get_response(request)