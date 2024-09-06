from django import forms

from mailing.models import Client, Message, Mail


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('owner',)


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        exclude = ('owner',)


class MailForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        user = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['clients'].queryset = Client.objects.filter(owner=user)
        self.fields['message'].queryset = Message.objects.filter(owner=user)

    class Meta:
        model = Mail
        exclude = ('is_active', 'owner')


class MailManagerForm(forms.ModelForm):

    class Meta:
        model = Mail
        fields = ('is_active',)


class ClientManagerForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('is_active',)
