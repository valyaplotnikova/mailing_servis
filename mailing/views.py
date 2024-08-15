
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView, DetailView

from mailing.forms import ClientForm, MessageForm, MailForm
from mailing.models import Client, Message, Mail, Log


# Create your views here.
class IndexView(TemplateView):
    template_name = 'mailing/home.html'


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('message_list')


class MailListView(ListView):
    model = Mail


class MailDetailView(DetailView):
    model = Mail


class MailCreateView(CreateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mail_list')


class MailUpdateView(UpdateView):
    model = Mail
    form_class = MailForm
    success_url = reverse_lazy('mail_list')


class MailDeleteView(DeleteView):
    model = Mail
    success_url = reverse_lazy('mail_list')


class LogListView(ListView):
    model = Log