from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.CharField(max_length=150, verbose_name='email', unique=True)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    father_name = models.CharField(max_length=150, verbose_name='Отчество')
    comment = models.TextField(verbose_name='Содержимое', **NULLABLE)

    def __str__(self):
        return f' {self.last_name} {self.first_name} {self.father_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты Сервиса'


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок письма")
    body = models.TextField(verbose_name='Тело письма', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Сообщение для рассылки'
        verbose_name_plural = 'Сообщения для рассылки'


class Mail(models.Model):
    PERIOD = [
        ('раз в день', 'раз в день'),
        ('раз в неделю', 'раз в неделю'),
        ('раз в месяц', 'раз в месяц'),
    ]
    STATUS = [
        ('создана', 'создана'),
        ('завершена', 'завершена'),
        ('запущена', 'запущена'),
    ]
    name = models.CharField(max_length=100, verbose_name='Название рассылки', default='Рассылка')
    clients = models.ManyToManyField(Client, verbose_name='Кому (клиенты сервиса)')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    date_start = models.DateField(verbose_name='Дата начала рассылки', default=timezone.now)
    date_next = models.DateTimeField(verbose_name="следующая дата рассылки", default=timezone.now)
    date_end = models.DateField(verbose_name='Дата окончания рассылки', default=timezone.now)
    start_time = models.TimeField(verbose_name='Время рассылки', default=timezone.now)
    period = models.CharField(max_length=30, choices=PERIOD, verbose_name='Периодичность рассылки',
                              default='раз в день')
    status = models.CharField(max_length=30, choices=STATUS, verbose_name='Статус рассылки',
                              default='создана')
    is_active = models.BooleanField(default=True, verbose_name='Активация рассылки')

    def __str__(self):
        return f'{self.name}: Дата начала: {self.date_start}, Дата окончания: {self.date_end}. Статус: {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        permissions = [
            ("set_is_active", "Активация рассылки")
        ]


class Log(models.Model):
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='Рассылка')
    last_time_mail = models.DateTimeField(auto_now=True, verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=50, verbose_name='Статус попытки')
    response = models.TextField(verbose_name='Ответ сервера', **NULLABLE)

    def __str__(self):
        return (f'Дата и время последней попытки: {self.last_time_mail}.'
                f' Статус попытки:{self.status}')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
