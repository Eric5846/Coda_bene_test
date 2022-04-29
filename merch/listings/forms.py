from django import forms
from listings.models import Ref

class RefForm(forms.Form):
	gtin = forms.CharField()
	expiration = forms.DateField(input_formats=['%d-%m-%Y'])
