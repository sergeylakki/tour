from django.forms import ModelForm

from main.models import Client


class ReservationForm(ModelForm):

    class Meta:
        model = Client
        exclude = ('on_delete',)