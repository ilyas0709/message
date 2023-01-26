import pytz
from django.db import models


from timezone_field import TimeZoneField


# Create your models here.

# Модель рассылки


class NotificationTags(models.Model):
    tag = models.CharField(verbose_name='Тег', max_length=100)

    def __str__(self):
        return self.tag


class PhoneCode(models.Model):
    code = models.CharField(verbose_name='Код мобильного оператора', max_length=100)

    def __str__(self):
        return self.code


class Mailing(models.Model):
    start_datetime = models.DateTimeField(verbose_name='Дата и время начала рассылки')
    end_datetime = models.DateTimeField(verbose_name='Дата и время окончания рассылки')
    message = models.TextField(verbose_name='Текст сообщения')
    tag = models.ManyToManyField(NotificationTags, blank=True, verbose_name='Тег')
    phone_code = models.ManyToManyField(PhoneCode, verbose_name='Код мобильного оператора')

    def get_tags(self):
        return "\n".join([str(p) for p in self.tag.all()])

    def get_phone_codes(self):
        return "\n".join([str(p) for p in self.phone_code.all()])


class Client(models.Model):
    TIME_ZONE_CHOICES = [(x, x) for x in pytz.common_timezones]

    phone_number = models.CharField('Номер телефона', max_length=100)
    tag = models.ManyToManyField(NotificationTags, verbose_name='Тег')
    phone_code = models.ForeignKey(PhoneCode, on_delete=models.CASCADE, verbose_name='Код мобильного оператора')
    timezone = TimeZoneField(choices=TIME_ZONE_CHOICES, verbose_name='Часовой пояс')

    # def tags(self):
    #     return ', '.join([tag.tag for tag in self.tag.all()])
    # def get_phone_codes(self):
    #     return "\n".join([str(p) for p in self.phone_code.all()])

    def get_tags(self):
        return "\n".join([str(p) for p in self.tag.all()])


MESSAGE_STATUS_CHOICES = (
    ('send', 'Отправлено'),
    ('fail', 'Не отправлено'),
)


class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент', related_name='messages')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка', related_name='messages')
    send_date = models.DateTimeField(verbose_name='Дата и время отправки сообщения', auto_now_add=True)
    status = models.BooleanField(verbose_name='Статус отправки сообщения', choices=MESSAGE_STATUS_CHOICES,
                                 default=MESSAGE_STATUS_CHOICES[0][0])


# Create your models here.
