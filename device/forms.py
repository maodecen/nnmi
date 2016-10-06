from django import forms

class nodeForm(forms.Form):
    node_name = forms.CharField(max_length=256)
