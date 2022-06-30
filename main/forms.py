from django import forms
from django.forms import Select

from main.models import DockerAddresses


class SelectDocker(forms.ModelForm):
    name = forms.ChoiceField(choices=[(d.id, f'{d.name}({d.uri})') for d in DockerAddresses.objects.all()])

    class Meta:
        model = DockerAddresses
        fields = ['name']
        widgets = {
            'name': Select(attrs={'class': 'select'}),
        }
