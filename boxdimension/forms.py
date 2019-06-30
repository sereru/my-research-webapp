from django import forms

class BoxForm(forms.Form):
    Img = forms.ImageField(label = 'Img')