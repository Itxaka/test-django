from django import forms
from django.forms import Select

from main.models import DockerAddresses


def get_choices():
    return [(d.id, f'{d.name}({d.uri})') for d in DockerAddresses.objects.all()]


class SelectDocker(forms.ModelForm):
    """
    Form to select a docker existing value
    """
    name = forms.ChoiceField(choices=get_choices)

    class Meta:
        model = DockerAddresses
        fields = ['name']
        widgets = {
            'name': Select(attrs={'class': 'select'}),
        }


class DockerAdd(forms.ModelForm):
    """
    Form to add a docker address
    """
    class Meta:
        model = DockerAddresses
        exclude = []
