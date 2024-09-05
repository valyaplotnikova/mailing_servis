from django import forms

from mailing.models import Client, Message, Mail
from users.models import User


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('owner',)


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        exclude = ('owner',)


class MailForm(forms.ModelForm):

    class Meta:
        model = Mail
        exclude = ('is_active', 'owner')
