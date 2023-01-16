from src.config.env import env

# https://django-environ.readthedocs.io/en/latest/tips.html#email-settings
# DJANGO_ADMINS=Blake:blake@cyb.org,Alice:alice@cyb.org
ADMINS = [x.split(':') for x in env.list('DJANGO_ADMINS')]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default='mx1.ntbroker.ru')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='exchange')
SERVER_EMAIL = env('SERVER_EMAIL', default='exchange@ntbroker.ru')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default=None)
EMAIL_USE_TLS = False
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = env('EMAIL_SUBJECT_PREFIX', default='Dbf2MSSql')

# from django.core.mail import send_mail
# send_mail(
#     subject='A cool subject',
#     message='A stunning message',
#     from_email='exchange@ntbroker.ru',
#     recipient_list=ADMINS,
#     auth_user=EMAIL_HOST_USER,
#     auth_password=EMAIL_HOST_PASSWORD
# )