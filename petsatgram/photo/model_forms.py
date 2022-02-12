from django import forms

from petsatgram.main.models import PetPhoto
from petsatgram.main.views import get_first_profile

profile = get_first_profile()


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('photo', 'tagged_pets', 'description', 'user_profile')
        widgets = {
            'photo': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Enter description'
                }
            ),

            'tagged_pets': forms.SelectMultiple(
                attrs={'class': 'form-control'}
            ),

            'user_profile': forms.HiddenInput(
                attrs={'value': profile.id}
            )

        }


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('tagged_pets', 'description', 'user_profile')
        widgets = {

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Enter description'
                }
            ),

            'tagged_pets': forms.SelectMultiple(
                attrs={'class': 'form-control'}
            ),

            'user_profile': forms.HiddenInput(
                attrs={'value': profile.id}
            )

        }
