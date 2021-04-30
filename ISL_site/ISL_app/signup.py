from django import forms
class Reg(forms.Form):
    firstname = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    confirmpassword = forms.CharField(max_length=30)

