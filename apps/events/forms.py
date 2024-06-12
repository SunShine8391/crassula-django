from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'description']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg mt-4',
                    'placeholder': 'Full name'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg mt-4',
                    'placeholder': 'Email'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg mt-4',
                    'placeholder': 'Phone'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-lg mt-4',
                    'placeholder': 'Description'
                }
            )
        }

    # def save(self, commit=True):
    #     self.instance.event = self.event
    #     return super().save(commit)
