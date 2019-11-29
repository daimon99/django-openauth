from django.apps import AppConfig


class UniauthConfig(AppConfig):
    name = 'uniauth'
    verbose_name = '统一认证'

    def ready(self):
        from django.contrib.auth import views
        from uniauth.views import UniAuthView
        views.LoginView = UniAuthView
