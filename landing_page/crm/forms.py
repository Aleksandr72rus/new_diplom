from django import forms


class OrderForm(forms.Form):
    theme = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    short = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
