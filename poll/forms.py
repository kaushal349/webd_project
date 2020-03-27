from django import forms
from .models import Poll

class CreatePollForm(forms.ModelForm):
    """Form definition for CreatePoll."""

    class Meta:
        """Meta definition for CreatePollform."""

        model = Poll
        fields = ('question','option1','option2','option3')
