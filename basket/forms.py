from django import forms

class UserForBasket(forms.Form):
    client_first_name = forms.CharField(required=True)
    client_last_name = forms.CharField(required=True)
    client_email = forms.EmailField(required=True)