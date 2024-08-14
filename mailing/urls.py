from django.urls import path

from mailing.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]
