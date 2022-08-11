from django.db import models

class Delivary(models.Model):
    date_time_start = models.DateTimeField(verbose_name='Начало рассылки')
    date_time_stop = models.DateTimeField(verbose_name='Конец рассылки')
    text = models.TextField(verbose_name='Сообщение')
    filter_code =models.IntegerField(verbose_name='Фильтр код')
    filter_teg = models.CharField(max_length=50, verbose_name='Фильтр Тэг')
    count_send_yes = models.IntegerField(verbose_name='Сообщений доставлено')
    count_send_no = models.IntegerField(verbose_name='Сообщений НЕ доставлено')

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'
        ordering = ['id']

    def __str__(self):
        return self.id

class Client(models.Model):
    phone = models.IntegerField(verbose_name='Телефон')
    code_phone = models.IntegerField(verbose_name='код')
    teg = models.CharField(max_length=50, verbose_name='Фильтр Тэг')
    time_zone  = models.IntegerField(verbose_name='Временная зона')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['id']

    def __str__(self):
        return self.id

class MessageStatusChoices(models.TextChoices):
    """Статусы сообщения."""

    OPEN = "SEND", "Отправлено"
    CLOSED = "NO SEND", "Не отправлено"


class Message(models.Model):
    date_time_send = models.DateTimeField(verbose_name='Время рассылки')
    status = models.TextField(
        choices = MessageStatusChoices.choices,
        default = MessageStatusChoices.CLOSED
    )
    response_code = models.IntegerField(verbose_name='код ответа')
    response_message = models.TextField(verbose_name='Сообщение ответа')
    delivary = models.ForeignKey(Delivary, on_delete=models.CASCADE, related_name='message')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='message')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['status']

    def __str__(self):
        return self.status
