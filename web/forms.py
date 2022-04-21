from django import forms
from .models import Contact
from django.forms import widgets


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name": widgets.TextInput(attrs={"class":"form-control", "placeholder": "Your Name"}),
            "phone": widgets.TextInput(attrs={"class":"form-control", "placeholder": "Your Phone"}),
            "email": widgets.EmailInput(attrs={"class":"form-control", "placeholder": "Your Email Address"}),
            "project_details": widgets.Textarea(attrs={"class":"form-control", "placeholder": "Tell About Project"}),
        }
