from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'name',
            'sex',
            'age',
            'date_save',
            'photo',
            'person',
            'vacine',

        ]
        labels = {
            'name': 'Name',
            'sex': 'Sex',
            'age':'aproximate age',
            'date_save': 'date of recover',
            'photo':'photo the Mascote',
            'person':'Adopter',
            'vacine': 'Vacine',

        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'sex':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'date_save':forms.TextInput(attrs={'class':'form-control'}),
            'photo':forms.ImageField(),
            'person':forms.Select(attrs={'class':'form-control'}),
            'vacine':forms.CheckboxSelectMultiple(),

        }

