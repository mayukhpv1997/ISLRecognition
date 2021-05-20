from django import forms


class Feedback(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=30)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=200)

