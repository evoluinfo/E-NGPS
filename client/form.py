from django.forms import ModelForm
from .models import Seller as Client


class ClientForm(ModelForm):

      class Meta:
            model = Client
            fields = '__all__'