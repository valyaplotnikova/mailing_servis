import datetime
import smtplib

from django.conf import settings
from django.core.mail import send_mail

from mailing.models import Log, Mail


def my_job():
    day = datetime.timedelta(days=1, hours=0, minutes=0)
    weak = datetime.timedelta(days=7, hours=0, minutes=0)
    month = datetime.timedelta(days=30, hours=0, minutes=0)

    mails = Mail.objects.all().filter(status='создана', is_active=True)

    for mail in mails:
        mail.status = 'запущена'
        mail.save()
        emails_list = [client.email for client in mail.clients.all()]

        result = send_mail(
            subject=mail.message.title,
            message=mail.message.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails_list,
            fail_silently=False,
        )

        if result == 1:
            status = 'отправлено'
        else:
            status = 'Ошибка отправки'

        log = Log(mail=mail, status=status, response=result)
        log.save()

        if mail.period == 'раз в день':
            mail.date_next = log.last_time_mail + day
        elif mail.period == 'раз в неделю':
            mail.date_next = log.last_time_mail + weak
        elif mail.period == 'раз в месяц':
            mail.date_next = log.last_time_mail + month

        if mail.date_next < mail.date_end:
            mail.status = 'создана'
        else:
            mail.status = 'завершена'
        mail.save()


def send_mailing():
    current_time = datetime.timezone.localtime(datetime.timezone.now())
    mailing_list = Mail.objects.all()
    for mailing in mailing_list:
        if mailing.date_end < current_time:
            mailing.status = Mail.DONE
            continue
        if mailing.time_start <= current_time < mailing.date_end:
            mailing.status = Mail.STARTED
            mailing.save()
            for client in mailing.client.all():
                try:
                    send_mail(
                        subject=mailing.message.title,
                        message=mailing.message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                        fail_silently=False
                    )

                    log = Log.objects.create(
                        date=mailing.time_start,
                        status=Log.SENT,
                        mailing=mailing,
                        client=client
                    )
                    log.save()
                    return log

                except smtplib.SMTPException as error:
                    log = Log.objects.create(
                        date=mailing.time_start,
                        status=Log.FAILED,
                        mailling=mailing,
                        client=client,
                        response=error
                    )
                    log.save()

                    return log

        else:
            mailing.status = Mail.DONE
            mailing.save()
