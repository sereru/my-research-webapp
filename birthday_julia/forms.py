from django import forms
#入力部分をpythonで作製し保持する

class JuliaForm(forms.Form):
    #name = forms.CharField(label='name')
    Real = forms.FloatField(label ='Real')
    Image = forms.FloatField(label='Image')
