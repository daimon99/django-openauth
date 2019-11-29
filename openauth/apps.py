from django.apps import AppConfig


class OpenauthConfig(AppConfig):
    name = 'openauth'
    verbose_name = '统一认证'

    def ready(self):
        from django.contrib.auth import views
        from openauth.views import OpenAuthView
        views.LoginView = OpenAuthView
