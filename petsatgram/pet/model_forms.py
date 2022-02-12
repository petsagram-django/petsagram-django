from django import forms

from petsatgram.main.models import Pet
from petsatgram.main.views import get_first_profile


profile = get_first_profile()


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth', 'user_profile')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'user_profile': forms.HiddenInput(
                attrs={
                    'value': profile.id
                }
            )

        }
