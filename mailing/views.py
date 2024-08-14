from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView, DetailView

from mailing.forms import ClientForm
from mailing.models import Client


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