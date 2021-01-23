from django.contrib.auth.forms import forms
from leads.models import Agent


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )
