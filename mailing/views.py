import random

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView, DetailView

from blog.models import Blog
from mailing.forms import ClientForm, MessageForm, MailForm, MailManagerForm, ClientManagerForm
from mailing.models import Client, Message, Mail, Log
from mailing.services import get_mailings_for_cache


class IndexView(TemplateView):
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mail_count'] = get_mailings_for_cache()
        context_data['active_mail_count'] = len(Mail.objects.filter(is_active=True))
        context_data['client_count'] = len(Client.objects.all())
        context_data['object_list'] = random.sample(list(Blog.objects.all()), 3)

        return context_data


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return ClientForm
        elif user == self.object.owner:
            return ClientForm
        elif user.has_perm('mailing.is_active_client') and user.has_perm('mailing.view_client'):
            return ClientManagerForm
        else:
            raise PermissionDenied


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MessageListView(ListView):
    model = Message

    def get_queryset(self, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return Message.objects.all()
        return Message.objects.filter(owner=self.request.user)


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()

        return super().form_valid(form)


class MessageUpdateView(PermissionRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')
    permission_required = 'mails.change_message'


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


class MailListView(LoginRequiredMixin, ListView):
    model = Mail


class MailDetailView(PermissionRequiredMixin, DetailView):
    model = Mail
    permission_required = 'mails.view_mail'


class MailCreateView(LoginRequiredMixin, CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailing:mail_list')

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()

        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class MailUpdateView(PermissionRequiredMixin, UpdateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mailing:mail_list')
    permission_required = 'mails.change_mail'

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return MailForm
        elif user == self.object.owner:
            return MailForm
        elif user.has_perm('mailing.is_active_mail') and user.has_perm('mailing.view_mail'):
            return MailManagerForm
        else:
            raise PermissionDenied


class MailDeleteView(LoginRequiredMixin, DeleteView):
    model = Mail
    success_url = reverse_lazy('mailing:mail_list')


class LogListView(ListView):
    model = Log
