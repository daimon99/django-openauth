# coding: utf-8
from django.conf import settings

# The jwt secret key。If this key not set or set with '',
# uniauth will get the key from redis
UNIAUTH_JWT_SECRET = getattr(settings, 'UNIAUTH_JWT_SECRET', '')
# 企业微信统一认证平台的url，注意这个 url 在使用中，会再增加跳转地址
QYWX_LOGIN_URL = 'https://open.taijihuabao.com/api/uniauth/qywx?next='

# UNIAUTH_REDIS_HOST = getattr(settings, 'UNIAUTH_REDIS_HOST', 'localhost')
# UNIAUTH_REDIS_PORT = getattr(settings, 'UNIAUTH_REDIS_PORT', '6379')
# UNIAUTH_REDIS_DB = getattr(settings, 'UNIAUTH_REDIS_DB', '9')
# UNIAUTH_REDIS_PASSWORD = getattr(settings, 'UNIAUTH_REDIS_PASSWORD', '')
