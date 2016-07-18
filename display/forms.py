from django import forms

class NameForm(forms.Form):
    data_name = forms.CharField(label='dropdown1', max_length=100)
