from django import forms


class LinkForm(forms.Form):

    link = forms.CharField(label = 'Input Link', max_length=100)