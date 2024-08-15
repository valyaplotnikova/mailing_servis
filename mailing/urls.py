from django.urls import path

from mailing.views import IndexView, ClientListView, ClientDeleteView, ClientCreateView, ClientUpdateView, \
    ClientDetailView, MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    MailListView, MailCreateView, MailDetailView, MailUpdateView, MailDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('mail/', MailListView.as_view(), name='mail_list'),
    path('mail_create/', MailCreateView.as_view(), name='mail_create'),
    path('mail_detail/<int:pk>/', MailDetailView.as_view(), name='mail_detail'),
    path('mail_update/<int:pk>/', MailUpdateView.as_view(), name='mail_update'),
    path('mail_delete/<int:pk>/', MailDeleteView.as_view(), name='mail_delete'),
]
