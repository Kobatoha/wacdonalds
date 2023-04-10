from .models import FarmRaidBoss
from django.forms import ModelForm, DateInput, TimeInput, Select, CheckboxSelectMultiple


class FarmRaidBossForm(ModelForm):
    class Meta:
        model = FarmRaidBoss
        fields = ['name', 'date', 'time', 'party_members']

        widgets = {
            'name': Select(attrs={'class': 'farm_form'}),
            'date': DateInput(attrs={'class': 'farm_form'}),
            'time': TimeInput(attrs={'class': 'farm_form'}),
            'party_members': CheckboxSelectMultiple(),
        }
