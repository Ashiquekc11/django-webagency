from django import forms
from .models import Contact
from django.forms import widgets


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("ip_address",)
        widgets = {
            "name": widgets.TextInput(attrs={"class":"form-control", "placeholder": "Your Name"}),
            "phone": widgets.TextInput(attrs={"class":"form-control", "placeholder": "Your Phone"}),
            "email": widgets.EmailInput(attrs={"class":"form-control", "placeholder": "Your Email Address"}),
            "project_details": widgets.Textarea(attrs={"class":"form-control", "placeholder": "Tell About Project"}),
        }

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Your email',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
