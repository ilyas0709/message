from django.shortcuts import render
from rest_framework import viewsets
from .models import Message, Mailing, PhoneCode, Client, NotificationTags
from .serializers import MailingSerializer, MessageSerializer, PhoneCodeSerializer, NotificationTagsSerializer, ClientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class PhoneCodeViewSet(viewsets.ModelViewSet):
    queryset = PhoneCode.objects.all()
    serializer_class = PhoneCodeSerializer


class NotificationTagsViewSet(viewsets.ModelViewSet):
    queryset = NotificationTags.objects.all()
    serializer_class = NotificationTagsSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# Create your views here.
