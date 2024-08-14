from django.urls import path

from mailing.views import IndexView, ClientListView, ClientDeleteView, ClientCreateView, ClientUpdateView, \
    ClientDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
]
