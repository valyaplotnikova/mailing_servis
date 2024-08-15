from django import forms

from mailing.models import Client, Message, Mail


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = "__all__"


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = "__all__"


class MailForm(forms.ModelForm):

    class Meta:
        model = Mail
        fields = "__all__"