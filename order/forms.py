from django import forms

class UserForBasket(forms.Form):
    client_username = forms.CharField(required=True)