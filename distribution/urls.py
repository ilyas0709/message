from django.urls import path, include
from rest_framework import routers
from .views import *

app_name = 'distribution'


router = routers.DefaultRouter()
router.register('client', ClientViewSet)
router.register('mailing', MailingViewSet)
router.register('message', MessageViewSet)
router.register('phone_code', PhoneCodeViewSet)
router.register('tag', NotificationTagsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
