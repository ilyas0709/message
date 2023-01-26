from rest_framework import serializers
from .models import Client, Mailing, Message, NotificationTags, PhoneCode
from timezone_field.rest_framework import TimeZoneSerializerField


class NotificationTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTags
        fields = ('id', 'tag')


class PhoneCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneCode
        fields = ('id', 'code')


class MailingSerializer(serializers.ModelSerializer):
    # tag = NotificationTagsSerializer(many=True)
    # phone_code = PhoneCodeSerializer(many=True)

    class Meta:
        model = Mailing
        fields = ('id', 'start_datetime', 'end_datetime', 'message',)


class ClientSerializer(serializers.ModelSerializer):
    tag = NotificationTagsSerializer(many=True)
    phone_code = PhoneCodeSerializer(many=True)
    tz1 = TimeZoneSerializerField()

    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'phone_code', 'tag', 'phone_code', 'tz1')


class MessageSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    mailing = MailingSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'client', 'mailing', 'send_date', 'status')

