from django import forms
from .models import Ticket


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title','content']

class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title','content']