from django.contrib import admin
from .models import Mailing, Message, PhoneCode, Client, NotificationTags


class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_datetime', 'end_datetime', 'get_tags', 'get_phone_codes')
    list_display_links = 'id get_tags'.split()
    search_fields = ('id', )


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'phone_code', 'timezone', 'get_tags')
    list_display_links = ('id', 'phone_number', 'get_tags')
    search_fields = ('id', 'phone_number')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'mailing', 'send_date', 'status')
    list_display_links = ('id', 'client', 'status', 'mailing')
    search_fields = ('id', 'client', 'status')


class NotificationTagsAdmin(admin.ModelAdmin):
    list_display = 'id tag'.split()
    search_fields = 'id tag'.split()


class PhoneCodeAdmin(admin.ModelAdmin):
    list_display = 'id code'.split()
    search_fields = 'id code'.split()


admin.site.register(Message, MessageAdmin)
admin.site.register(Mailing, MailingAdmin)
admin.site.register(NotificationTags, NotificationTagsAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(PhoneCode, PhoneCodeAdmin)
# Register your models here.
